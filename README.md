# Log IP Analyzer

A beginner-friendly Python script that extracts and counts IP addresses from log files to help identify suspicious login attempts.  
This project demonstrates basic scripting for cybersecurity tasks and log analysis.

## Features
- Reads log files
- Extracts IP addresses using regex
- Counts occurrences of each IP
- Helps detect brute-force or suspicious login activity

## Requirements
- Python 3.8+  
- Works with standard log files (e.g., SSH auth logs)

## Example Log
Mar 10 12:45:01 server sshd[1234]: Failed password for root from 192.168.1.5 port 22 ssh2
Mar 10 12:45:05 server sshd[1234]: Failed password for admin from 185.23.44.91 port 34521 ssh2
Mar 10 12:45:07 server sshd[1234]: Failed password for root from 192.168.1.5 port 22 ssh2

## Example Output
192.168.1.5 -> 2 times
185.23.44.91 -> 1 time

## Usage
1. Place your log file in the same folder as `ip_analiz.py` and name it `log.txt`.  
2. Run the script:

```bash
python ip_analiz.py

Purpose

This project was created to practice Python scripting in a cybersecurity context.
It helps beginners understand log parsing, regex usage, and basic security automation tasks.
