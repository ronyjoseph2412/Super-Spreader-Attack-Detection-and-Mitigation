# #!/usr/bin/env python
# import argparse
# import sys
# import socket
# import struct
# from scapy.all import sniff, get_if_list, get_if_hwaddr
# from scapy.all import Packet
# from scapy.all import Ether, IP, UDP, TCP
#
# def get_if():
#     ifs=get_if_list()
#     iface=None # "h1-eth0"
#     for i in get_if_list():
#         if "eth0" in i:
#             iface=i
#             break;
#         if not iface:
#             print("Cannot find eth0 interface")
#             exit(1)
#     return iface
#
# def handle_pkt(pkt):
#     if IP in pkt:
#         ip_layer = pkt.getlayer(IP)
#         src_ip = ip_layer.src
#         dst_ip = ip_layer.dst
#         tos = ip_layer.tos
#         flags = ip_layer.flags
#         proto = ip_layer.proto
#     if UDP in pkt:
#         udp_layer = pkt.getlayer(UDP)
#         src_port = udp_layer.sport
#         dst_port = udp_layer.dport
#         print("Received UDP packet:")
#         print("Source IP: ", src_ip)
#         print("Destination IP: ", dst_ip)
#         print("Type of Service: ", tos)
#         print("IP Flags: ", flags)
#         print("Protocol: ", proto)
#         print("Source Port: ", src_port)
#         print("Destination Port: ", dst_port)
#         print("\n")
#
#     if TCP in pkt:
#         tcp_layer = pkt.getlayer(TCP)
#         src_port = tcp_layer.sport
#         dst_port = tcp_layer.dport
#         print("Received TCP Packet:")
#         print("Source IP: ", src_ip)
#         print("Destination IP: ", dst_ip)
#         print("Type of Service: ", tos)
#         print("IP Flags: ", flags)
#         print("Protocol: ", proto)
#         print("Source Port: ", src_port)
#         print("Destination Port: ", dst_port)
#         print("\n")
#
#
# def main():
#     iface = get_if()
#     print("Hello")
#     sniff(iface = iface, prn = lambda x: handle_pkt(x))
#
# if __name__ == 'main':
#     main()


#!/usr/bin/env python
import sys
import struct
import os

from scapy.all import sniff, sendp, hexdump, get_if_list, get_if_hwaddr
from scapy.all import Packet, IPOption
from scapy.all import ShortField, IntField, LongField, BitField, FieldListField, FieldLenField
from scapy.all import IP, UDP, Raw
from scapy.layers.inet import _IPOption_HDR

def get_if():
    ifs=get_if_list()
    iface=None
    for i in get_if_list():
        if "eth0" in i:
            iface=i
            break;
    if not iface:
        print "Cannot find eth0 interface"
        exit(1)
    return iface

def handle_pkt(pkt):
    print "got a packet"
    pkt.show2()
#    hexdump(pkt)
    sys.stdout.flush()

def main():
    ifaces = filter(lambda i: 'eth' in i, os.listdir('/sys/class/net/'))
    iface = ifaces[0]
    print "sniffing on %s" % iface
    sys.stdout.flush()
    sniff(iface = iface,
          prn = lambda x: handle_pkt(x))

if __name__ == '__main__':
    main()
