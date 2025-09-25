
# Port Scanner

A simple TCP port scanner written in Python.  
It scans ports, checks whether they are open, grabs banners, and can log results to a file.

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
# Scan and show results in console
python3 scanner.py -t 127.0.0.1 -p 22-80

# Save results to text file
python3 scanner.py -t 127.0.0.1 -p 22-80 -o result.txt

# Save results to JSON
python3 scanner.py -t 127.0.0.1 -p 22-80 -o result.json
```

Sample output:

```
[OPEN]   Port 22 → SSH-2.0-OpenSSH_8.9p1
[CLOSED] Port 23
[CLOSED] Port 25
```

---

## Features

* TCP connect scan
* Banner grabbing (basic service detection)
* Multithreading for faster scans
* Output results to `.txt` or `.json`

---

## To-Do

* [x] Add multithreading for faster scans
* [x] Save results to text/JSON file
* [ ] Implement UDP scanning

