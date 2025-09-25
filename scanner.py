import socket
import argparse
import threading
import json

results = []
log_file = None

def log(message):
    print(message)
    if log_file:
        with open(log_file, "a") as f:
            f.write(message + "\n")

def scan_tcp(target, port):
    # TCP connect scan
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            try:
                banner = sock.recv(1024).decode().strip()
                if banner:
                    msg = f"[OPEN]   TCP {port} → {banner}"
                else:
                    msg = f"[OPEN]   TCP {port} (no banner)"
            except Exception:
                msg = f"[OPEN]   TCP {port} (no banner)"
        else:
            msg = f"[CLOSED] TCP {port}"
        log(msg)
        results.append({"port": port, "protocol": "TCP", "status": msg})
        sock.close()
    except Exception as e:
        err = f"[ERROR] TCP {port}: {e}"
        log(err)
        results.append({"port": port, "protocol": "TCP", "status": err})

def scan_udp(target, port):
    # UDP scan (send empty packet and wait for response)
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.settimeout(2)
        sock.sendto(b"", (target, port))
        try:
            data, _ = sock.recvfrom(1024)
            msg = f"[OPEN]   UDP {port} → response: {data[:30]!r}"
        except socket.timeout:
            msg = f"[UNKNOWN] UDP {port} (no response)"
        log(msg)
        results.append({"port": port, "protocol": "UDP", "status": msg})
        sock.close()
    except Exception as e:
        err = f"[ERROR] UDP {port}: {e}"
        log(err)
        results.append({"port": port, "protocol": "UDP", "status": err})

def parse_ports(ports_str):
    if "-" in ports_str:
        start, end = map(int, ports_str.split("-"))
        return range(start, end + 1)
    return [int(ports_str)]

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Port Scanner (TCP/UDP) with Banner Grabbing and Logging")
    parser.add_argument("-t", "--target", required=True, help="Target IP or hostname")
    parser.add_argument("-p", "--ports", required=True, help="Port or range (e.g., 22 or 1-100)")
    parser.add_argument("-th", "--threads", type=int, default=50, help="Number of threads (default=50)")
    parser.add_argument("-o", "--output", help="Output file (txt or json)")
    parser.add_argument("--udp", action="store_true", help="Enable UDP scanning instead of TCP")
    args = parser.parse_args()

    if args.output and not args.output.endswith(".json"):
        log_file = args.output

    ports = parse_ports(args.ports)

    thread_list = []
    for port in ports:
        if args.udp:
            thread = threading.Thread(target=scan_udp, args=(args.target, port))
        else:
            thread = threading.Thread(target=scan_tcp, args=(args.target, port))
        thread_list.append(thread)
        thread.start()

        if len(thread_list) >= args.threads:
            for t in thread_list:
                t.join()
            thread_list = []

    for t in thread_list:
        t.join()

    if args.output and args.output.endswith(".json"):
        with open(args.output, "w") as f:
            json.dump(results, f, indent=4)
        log(f"\n[+] Results saved to {args.output}")
