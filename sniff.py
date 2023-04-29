# import subprocess
# import time
# from scapy.all import *
# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation
#
# def plot_packet_length(src_ip):
#     # Open a subprocess to start Wireshark and capture packets
#     wireshark_process = subprocess.Popen(['sudo','wireshark', '-k', '-i', 'any', '-w', './capture.pcapng'])
#
#     # Wait for Wireshark to start
#     time.sleep(4)
#
#     # Read the captured packets from the capture file
#     packets = rdpcap('capture.pcapng')
#
#     # Filter packets based on source and destination IP addresses
#     ip_packets = []
#     for packet in packets:
#         if packet.haslayer(IP):
#             if packet[IP].src == src_ip:
#                 ip_packets.append(packet)
#                 print(packet[IP].dst)
#
#     # Define the figure and axis for the graph
#     fig, ax = plt.subplots()
#     ax.set_xlabel('Time')
#     ax.set_ylabel('Packet Length')
#     ax.set_title('Packet Length vs. Time for ')
#
#     # Define a function to update the graph
#     def update_graph(i):
#         # Read the captured packets from the capture file
#         packets = rdpcap('capture.pcapng')
#
#         # Filter packets based on source and destination IP addresses
#         ip_packets = []
#         for packet in packets:
#             if packet.haslayer(IP):
#                 if packet[IP].src == src_ip:
#                     ip_packets.append(packet)
#                     print(packet[IP].dst)
#
#         # Update the graph with the new data
#         x = []
#         y = []
#         for packet in ip_packets:
#             x.append(packet.time)
#             y.append(packet[IP].len)
#         ax.clear()
#         ax.plot(x, y)
#         ax.set_xlabel('Time')
#         ax.set_ylabel('Packet Length')
#         ax.set_title('Packet Length vs. Time for')
#
#     # Animate the graph
#     ani = FuncAnimation(fig, update_graph, interval=1000)
#     plt.show()
#
#
#
#
#
#
#
# while True:
#     plot_packet_length('10.0.1.1')
#     time.sleep(25)



# NEW Code


# import subprocess
# import time
# from scapy.all import *
# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation
#
# # Define the source and destination IP addresses
# src_ip = '10.0.1.1'
# dst_ips = ['10.0.2.2', '10.0.3.3', '10.0.3.4']
#
# # Open a subprocess to start Wireshark and capture packets
# wireshark_process = subprocess.Popen(['sudo','wireshark', '-k', '-i', 'any', '-w', './capture.pcapng'])
#
# # Wait for Wireshark to start
# time.sleep(4)
#
# # Initialize the figure and axis for the packet count plot
# fig, ax = plt.subplots()
# ax.set_xlabel('Time')
# ax.set_ylabel('Packet Count')
# ax.set_title('Packet Count vs. Time')
# lines = {}
#
# # Define a function to update the packet count plot with new data
# def update_packet_count_plot(i):
#     global lines
#     packets = rdpcap('capture.pcapng')
#     packet_count = {}
#     for dst_ip in dst_ips:
#         ip_packets = []
#         for packet in packets:
#             if packet.haslayer(IP):
#                 if packet[IP].src == src_ip and packet[IP].dst == dst_ip:
#                     ip_packets.append(packet)
#         dst_packet_count = {}
#         for packet in ip_packets:
#             if packet.time not in dst_packet_count:
#                 dst_packet_count[packet.time] = 1
#             else:
#                 dst_packet_count[packet.time] += 1
#         packet_count[dst_ip] = dst_packet_count
#     for dst_ip in dst_ips:
#         x = []
#         y = []
#         for time, count in packet_count[dst_ip].items():
#             x.append(time)
#             y.append(count)
#         if dst_ip not in lines:
#             lines[dst_ip], = ax.plot(x, y, label=dst_ip)
#         else:
#             lines[dst_ip].set_data(x, y)
#     ax.legend()
#     ax.relim()
#     ax.autoscale_view()
#     return lines.values()
#
# # Define the animation object that repeatedly calls the update function
# ani = FuncAnimation(fig, update_packet_count_plot, interval=5000)
#
# # Show the plot
# plt.show()




# BEST Code

# import subprocess
# import time
# from scapy.all import *
# import matplotlib.pyplot as plt
#
# # Define the source and destination IP addresses
# src_ip = '10.0.1.1'
# dst_ips = ['10.0.2.2', '10.0.3.3', '10.0.4.4']
#
# # Open a subprocess to start Wireshark and capture packets
# wireshark_process = subprocess.Popen(['sudo','wireshark', '-k', '-i', 'any', '-w', './capture.pcapng'])
#
# # Wait for Wireshark to start
# time.sleep(4)
#
# # Read the captured packets from the capture file
# packets = rdpcap('capture.pcapng')
#
# # Count the number of packets exchanged between each source-destination pair over time
# packet_count = {}
# for dst_ip in dst_ips:
#     ip_packets = []
#     for packet in packets:
#         if packet.haslayer(IP):
#             if packet[IP].src == src_ip and packet[IP].dst == dst_ip:
#                 ip_packets.append(packet)
#     dst_packet_count = {}
#     for packet in ip_packets:
#         if packet.time not in dst_packet_count:
#             dst_packet_count[packet.time] = 1
#         else:
#             dst_packet_count[packet.time] += 1
#     packet_count[dst_ip] = dst_packet_count
#
# # Plot the packet count over time for each destination IP address
# fig, axs = plt.subplots(len(dst_ips), 2, figsize=(10, 8))
# fig.suptitle('Packet Analysis', fontsize=16)
#
# for i, dst_ip in enumerate(dst_ips):
#     x = []
#     y = []
#     for time, count in packet_count[dst_ip].items():
#         x.append(time)
#         y.append(count)
#     axs[i, 0].plot(x, y)
#     axs[i, 0].set_xlabel('Time')
#     axs[i, 0].set_ylabel('Packet Count')
#     axs[i, 0].set_title('Packet Count vs. Time for ',dst_ip)
#
#     # Filter packets based on source and destination IP addresses
#     ip_packets = []
#     for packet in packets:
#         if packet.haslayer(IP):
#             if packet[IP].src == src_ip and packet[IP].dst == dst_ip:
#                 ip_packets.append(packet)
#
#     # Calculate inter-arrival time for each packet
#     inter_arrival_time = []
#     for j in range(len(ip_packets)-1):
#         time_diff = ip_packets[j+1].time - ip_packets[j].time
#         inter_arrival_time.append(time_diff)
#
#     # Plot the inter-arrival time against time
#     x = [packet.time for packet in ip_packets[:-1]]
#     y = inter_arrival_time
#     axs[i, 1].scatter(x, y)
#     axs[i, 1].set_xlabel('Time')
#     axs[i, 1].set_ylabel('Inter-arrival Time (s)')
#     axs[i, 1].set_title('Packet Inter-arrival Time vs. Time for ',dst_ip)
#
# plt.tight_layout()
# plt.show()


import subprocess
import time
from scapy.all import *
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the source and destination IP addresses
src_ip = '10.0.1.1'
dst_ips = ['10.0.2.2', '10.0.3.3', '10.0.3.4']

# Open a subprocess to start Wireshark and capture packets
wireshark_process = subprocess.Popen(['sudo','wireshark', '-k', '-i', 'any', '-w', './capture.pcapng'])

# Wait for Wireshark to start
time.sleep(4)

# Define the figure and axis for the graph
fig, ax = plt.subplots()
ax.set_xlabel('Time')
ax.set_ylabel('Inter-arrival Time (s)')
ax.set_title('Packet Inter-arrival Time vs. Time')

# Define a function to update the graph
def update_graph(i):
    # Read the captured packets from the capture file
    packets = rdpcap('capture.pcapng')

    # Calculate inter-arrival time for each packet for each destination IP address
    inter_arrival_time = {}
    for dst_ip in dst_ips:
        ip_packets = []
        for packet in packets:
            if packet.haslayer(IP):
                if packet[IP].src == src_ip and packet[IP].dst == dst_ip:
                    ip_packets.append(packet)
        dst_inter_arrival_time = []
        for i in range(len(ip_packets)-1):
            time_diff = ip_packets[i+1].time - ip_packets[i].time
            dst_inter_arrival_time.append(time_diff)
        inter_arrival_time[dst_ip] = dst_inter_arrival_time

    # Plot the inter-arrival time against time for each destination IP address
    ax.clear()
    for dst_ip in dst_ips:
        ip_packets = []
        for packet in packets:
            if packet.haslayer(IP):
                if packet[IP].src == src_ip and packet[IP].dst == dst_ip:
                    ip_packets.append(packet)
        x = [packet.time for packet in ip_packets[:-1]]
        y = inter_arrival_time[dst_ip]
        ax.scatter(x, y, label=dst_ip)
    ax.set_xlabel('Time')
    ax.set_ylabel('Inter-arrival Time (s)')
    ax.set_title('Packet Inter-arrival Time vs. Time')
    ax.legend()

# Animate the graph
ani = FuncAnimation(fig, update_graph, interval=1000)
plt.show()
