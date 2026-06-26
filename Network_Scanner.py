# =======================
# === Network Scanner ===
# =======================

import subprocess
import socket
import sys

print("=== Network Scanner ===")

network = input("Enter network (e.g. 192.168.1): ")

print("\nScanning network...\n")

total = 254

