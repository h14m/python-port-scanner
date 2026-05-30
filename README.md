# Python Port Scanner

A Python-based network reconnaissance tool that scans a target host for open TCP ports and identifies common services running on those ports.

## Overview

This project was developed to understand the fundamentals of:

- TCP/IP Networking
- Socket Programming
- Port Scanning Techniques
- Service Enumeration
- Cybersecurity Reconnaissance

The scanner attempts to connect to a specified range of ports on a target host and reports which ports are open.

---

## Features

- Scan custom IP addresses or hostnames
- Specify start and end port ranges
- Detect open TCP ports
- Identify common services (SSH, HTTP, HTTPS, etc.)
- Save scan results to a report file
- Simple command-line interface

---

## Technologies Used

- Python 3
- Socket Programming
- TCP Networking

---

## Project Structure

```text
python-port-scanner/
│
├── port_scanner.py
├── scan_results.txt
├── README.md
└── requirements.txt
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/h14m/python-port-scanner.git
```

Navigate to the project folder:

```bash
cd python-port-scanner
```

---

## Usage

Run the scanner:

```bash
python3 port_scanner.py
```

Example:

```text
Enter target IP or hostname: 127.0.0.1
Enter start port: 1
Enter end port: 100
```

---

## Sample Output

```text
Scanning 127.0.0.1
--------------------------------------------------
OPEN : Port 22 (ssh)
OPEN : Port 80 (http)

Results saved to scan_results.txt
```

---

## Generated Report

The scanner automatically creates a report file:

```text
scan_results.txt
```

Example:

```text
Target: 127.0.0.1

OPEN : Port 22 (ssh)
OPEN : Port 80 (http)
```

---

## Learning Outcomes

Through this project, I gained practical experience in:

- Network reconnaissance
- Socket programming
- TCP connection handling
- Service identification
- Python automation
- Basic cybersecurity scanning techniques

---

## Future Enhancements

- Multithreaded scanning for faster performance
- Banner grabbing
- Service fingerprinting
- CSV/JSON report export
- Vulnerability lookup integration
- Web-based dashboard

---

## Disclaimer

This project is intended for educational purposes and authorized security testing only. Always obtain proper permission before scanning systems that you do not own or manage.

---

## Author

Mahi Honnagol

Cybersecurity Enthusiast | SOC Analyst Aspirant | Python Developer
