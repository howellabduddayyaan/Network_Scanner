# =======================
# === Host Identifier ===
# =======================

import socket

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)

print("\n=======================")
print("=== Host Identifier ===")
print("=======================")


print("\nComputer Name:", hostname)
print("IP Address:", ip)

# _________________________________________________________________________________________________