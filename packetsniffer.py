import subprocess
import time
from scapy.all import *
import matplotlib.pyplot as plt

# Define the source and destination IP addresses
src_ip = '10.0.1.1'
# dst_ip = '10.0.2.2'

# # Open a subprocess to start Wireshark and capture packets
wireshark_process = subprocess.Popen(['sudo','wireshark', '-k', '-i', 'any', '-w', './capture.pcapng'])
#
# # Wait for Wireshark to start
time.sleep(4)
#
# # Wait for the packets to be captured by Wireshark
# time.sleep(2)

# Read the captured packets from the capture file
packets = rdpcap('capture.pcapng')

# Filter packets based on source and destination IP addresses
ip_packets = []
for packet in packets:
    if packet.haslayer(IP):
        print(packet)
        if packet[IP].src == src_ip:
            ip_packets.append(packet)
# Plot only the filtered packets using source and destination IP addresses
x = []
y = []
for packet in ip_packets:
    print(packet)
    x.append(packet.time)
    y.append(packet[IP].len)


plt.plot(x, y)
plt.xlabel('Time')
plt.ylabel('Packet Length')
plt.title('Packet Length vs. Time')
plt.show()
