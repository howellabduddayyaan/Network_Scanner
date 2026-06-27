# =======================
# === Network Scanner ===
# =======================

import sys
import subprocess
import socket

print("\n=======================")
print("=== Network Scanner ===")
print("=======================")

network = input("\nEnter network (192.168.1): ")

print("\nScanning network...\n")

total = 254
devices = []

try:
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    print(f"Your IP address: {local_ip}\n")
except:
    print("Could not find your IP address\n")

for i in range(1, 255):
    ip = f"{network}.{i}"

# _________________________________________________________________________________________________

# ------------
# Progress Bar
# ------------

    progress = int((i / total) * 100)
    bar_length = 30
    filled = int(bar_length * i // total)
    bar = "█" * filled + "-" * (bar_length - filled)

    sys.stdout.write(f"\rScanning: |{bar}| {progress}% ({i}/{total})")
    sys.stdout.flush()

# _________________________________________________________________________________________________

    try:
        result = subprocess.run(["ping", "-n", "1", "-w", "100",ip],
                                capture_output=True,
                                text=True
                                )

        if "ttl=" in result.stdout.lower() :

            try:
                hostname = socket.gethostbyaddr(ip)[0]
            except:
                hostname = "Unknown"
                
            devices.append((ip, hostname))
    except:
        pass

print("\n\nScan Complete.")

# _________________________________________________________________________________________________
