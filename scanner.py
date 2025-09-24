import socket
import argparse

def scan_target(target, ports):
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"[OPEN] Port {port}")
        else:
            print(f"[CLOSED] Port {port}")
        sock.close()

def parse_ports(ports_str):
    ports = []
    if "-" in ports_str:
        start, end = map(int, ports_str.split("-"))
        ports = range(start, end + 1)
    else:
        ports = [int(ports_str)]
    return ports

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple Port Scanner")
    parser.add_argument("-t", "--target", required=True, help="Target IP or hostname")
    parser.add_argument("-p", "--ports", required=True, help="Port or range (e.g., 22 or 1-100)")
    args = parser.parse_args()

    ports = parse_ports(args.ports)
    scan_target(args.target, ports)