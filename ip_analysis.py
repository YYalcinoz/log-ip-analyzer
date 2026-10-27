import re
from collections import Counter

with open("log.txt", "r", encoding="utf-8") as file:
    data = file.read()

ips = re.findall(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b", data)

ip_count = Counter(ips)

print("IP addresses found:\n")
for ip, count in ip_count.most_common():
    print(f"{ip} -> {count} {'time' if count == 1 else 'times'}")
