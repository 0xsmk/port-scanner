import socket
import argparse
import threading
import json

results = []      # store scan results
log_file = None   # path to log file if provided

def log(message):
    # print to console and write to file if log_file is set
    print(message)
    if log_file:
        with open(log_file, "a") as f:
            f.write(message + "\n")

def scan_port(target, port):
    # check a single port and grab banner if possible
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            try:
                banner = sock.recv(1024).decode().strip()
                if banner:
                    msg = f"[OPEN]   Port {port} → {banner}"
                else:
                    msg = f"[OPEN]   Port {port} (no banner)"
            except Exception:
                msg = f"[OPEN]   Port {port} (no banner)"
        else:
            msg = f"[CLOSED] Port {port}"
        log(msg)
        results.append({"port": port, "status": msg})
        sock.close()
    except Exception as e:
        err = f"[ERROR] Port {port}: {e}"
        log(err)
        results.append({"port": port, "status": err})

def parse_ports(ports_str):
    # parse ports like "22" or "20-80"
    if "-" in ports_str:
        start, end = map(int, ports_str.split("-"))
        return range(start, end + 1)
    return [int(ports_str)]

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Multithreaded Port Scanner with Banner Grabbing and Logging")
    parser.add_argument("-t", "--target", required=True, help="Target IP or hostname")
    parser.add_argument("-p", "--ports", required=True, help="Port or range (e.g., 22 or 1-100)")
    parser.add_argument("-th", "--threads", type=int, default=50, help="Number of threads (default=50)")
    parser.add_argument("-o", "--output", help="Output file (txt or json)")
    args = parser.parse_args()

    # use text log file if provided
    if args.output and not args.output.endswith(".json"):
        log_file = args.output

    ports = parse_ports(args.ports)

    # start scanning ports in threads
    thread_list = []
    for port in ports:
        thread = threading.Thread(target=scan_port, args=(args.target, port))
        thread_list.append(thread)
        thread.start()

        # wait if too many active threads
        if len(thread_list) >= args.threads:
            for t in thread_list:
                t.join()
            thread_list = []

    # wait for remaining threads
    for t in thread_list:
        t.join()

    # save results to JSON if requested
    if args.output and args.output.endswith(".json"):
        with open(args.output, "w") as f:
            json.dump(results, f, indent=4)
        log(f"\n[+] Results saved to {args.output}")
