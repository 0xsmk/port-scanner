
# Port Scanner

A simple TCP/UDP port scanner written in Python.  
It scans ports, checks whether they are open, grabs banners (TCP), and can log results to a file.

**For educational purposes only.  
Do not scan hosts without explicit permission!**

---

## Installation

Clone the repository and run the scanner:

```bash
git clone git@github.com:0xsmk/port-scanner.git
cd port-scanner
python3 scanner.py -t 127.0.0.1 -p 1-100
````

---

## Example Usage

### TCP scan

```bash
# Scan ports with TCP
python3 scanner.py -t 127.0.0.1 -p 22-80
```

### UDP scan

```bash
# Scan DNS port with UDP
python3 scanner.py -t 127.0.0.1 -p 53 --udp
```

### Save results to file

```bash
# Save to text file
python3 scanner.py -t 127.0.0.1 -p 22-80 -o result.txt

# Save to JSON
python3 scanner.py -t 127.0.0.1 -p 22-80 -o result.json
```

Sample TCP output:

```
[OPEN]   TCP 22 → SSH-2.0-OpenSSH_8.9p1
[CLOSED] TCP 23
[CLOSED] TCP 25
```

Sample UDP output:

```
[OPEN]   UDP 53 → response: b'\x85\x80...'
[UNKNOWN] UDP 123 (no response)
```

---

## Features

* TCP connect scan
* UDP scanning (basic, response-based)
* Banner grabbing for TCP services
* Multithreading for faster scans
* Output results to `.txt` or `.json`

---

## To-Do

* [x] Add multithreading for faster scans
* [x] Save results to text/JSON file
* [x] Implement UDP scanning
* [ ] Improve UDP detection reliability

