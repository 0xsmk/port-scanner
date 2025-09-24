import socket
import argparse
import threading

def scan_port(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            try:
                banner = sock.recv(1024).decode().strip()
                if banner:
                    print(f"[OPEN]   Port {port} → {banner}")
                else:
                    print(f"[OPEN]   Port {port} (no banner)")
            except Exception:
                print(f"[OPEN]   Port {port} (no banner)")
        else:
            print(f"[CLOSED] Port {port}")
        sock.close()
    except Exception as e:
        print(f"[ERROR] Port {port}: {e}")

def parse_ports(ports_str):
    if "-" in ports_str:
        start, end = map(int, ports_str.split("-"))
        return range(start, end + 1)
    return [int(ports_str)]

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Multithreaded Port Scanner with Banner Grabbing")
    parser.add_argument("-t", "--target", required=True, help="Target IP or hostname")
    parser.add_argument("-p", "--ports", required=True, help="Port or range (e.g., 22 or 1-100)")
    parser.add_argument("-th", "--threads", type=int, default=50, help="Number of threads (default=50)")
    args = parser.parse_args()

    ports = parse_ports(args.ports)

    thread_list = []
    for port in ports:
        thread = threading.Thread(target=scan_port, args=(args.target, port))
        thread_list.append(thread)
        thread.start()

# Limit the number of active threads
        if len(thread_list) >= args.threads:
            for t in thread_list:
                t.join()
            thread_list = []

# Waiting for everyone
    for t in thread_list:
        t.join()
