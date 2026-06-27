# =======================
# === Network Scanner ===
# =======================

import sys
import subprocess
import socket

print("\n=== Network Scanner ===")

network = input("Enter network (123.456.7): ")

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

    progress = int((i / total) * 100)
    bar_length = 30
    filled = int(bar_length * i // total)
    bar = "█" * filled + "-" * (bar_length - filled)

    sys.stdout.write(f"\rScanning: |{bar}| {progress}% ({i}/254)")
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

            print(f"\n{ip} = {hostname} (ONLINE)")

    except:
        pass

print("\n\nScan Complete.")

# _________________________________________________________________________________________________
