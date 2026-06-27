# =======================
# === Network Scanner ===
# =======================

import subprocess
import socket


print("=== Network Scanner ===")

network = input("Enter network (e.g. 192.168.1): ")

print("\nScanning network...\n")

total = 254

try:
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    print(f"Your IP: {local_ip}\n")
except:
    pass

for i in range(1, 255):

    ip = f"{network}.{i}"

# _________________________________________________________________________________________________


print(f"Scanning {ip}...", end="\r")

    try:
        
        result = subprocess.run(
            ["ping", "-n", "1", "-w", "100", ip],
            capture_output=True,
            text=True
        )

        if "TTL=" in result.stdout:

            try:
                hostname = socket.gethostbyaddr(ip)[0]
            except:
                hostname = "Unknown"

            print(f"{ip}  →  {hostname} (ONLINE)")

    except:
        pass

    print("\n\nScan Complete.")





# _________________________________________________________________________________________________
