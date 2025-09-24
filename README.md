#  Port Scanner

A simple TCP port scanner written in Python.  
It scans ports, checks whether they are open, and attempts to grab the service banner.  

 **For educational purposes only.  
Do not scan hosts without explicit permission!**

---

##  Installation
Clone the repository and run the scanner:

```bash
git clone git@github.com:0xsmk/port-scanner.git
cd port-scanner
python3 scanner.py -t 127.0.0.1 -p 1-100
