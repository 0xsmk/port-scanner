
# Port Scanner

A simple TCP port scanner written in Python.  
It scans ports, checks whether they are open, and attempts to grab the service banner.

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

```bash
python3 scanner.py -t 127.0.0.1 -p 22-80
```

Sample output:

```
[OPEN] Port 22 → SSH-2.0-OpenSSH_8.9p1 Ubuntu-3
[OPEN] Port 80 (no banner)
[CLOSED] Port 443
```

---

## Features

* TCP connect scan
* Banner grabbing (basic service detection)
* Custom target and port range

---

## To-Do

* [x] Add multithreading for faster scans
* [ ] Implement UDP scanning
* [ ] Export results to JSON/CSV
