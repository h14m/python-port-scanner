import socket
from datetime import datetime

target = input("Enter target IP or hostname: ")
start_port = int(input("Enter start port: "))
end_port = int(input("Enter end port: "))

start_time = datetime.now()

print(f"\nScanning {target}")
print("-" * 50)

results = []

for port in range(start_port, end_port + 1):
    print(f"Scanning Port {port}...")

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.1)

    result = sock.connect_ex((target, port))

    if result == 0:
        try:
            service = socket.getservbyport(port)
        except:
            service = "Unknown"

        output = f"OPEN : Port {port} ({service})"

        print(output)
        results.append(output)

    sock.close()

end_time = datetime.now()

with open("scan_results.txt", "w") as file:
    file.write(f"Target: {target}\n")
    file.write(f"Scan Started: {start_time}\n")
    file.write(f"Scan Ended: {end_time}\n\n")

    for item in results:
        file.write(item + "\n")

print("\nResults saved to scan_results.txt")
