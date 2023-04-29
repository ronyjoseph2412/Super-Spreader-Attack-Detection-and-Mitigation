#!/usr/bin/env python
import argparse
import sys
import socket
import random
import struct
import time
from scapy.all import sendp, send, get_if_list, get_if_hwaddr
from scapy.all import Packet
from scapy.all import Ether, IP, UDP, TCP
import random
import threading

def get_if():
    ifs=get_if_list()
    iface=None # "h1-eth0"
    for i in get_if_list():
        if "eth0" in i:
            iface=i
            break;
    if not iface:
        print("Cannot find eth0 interface")
        exit(1)
    return iface

def sendpackets(addr):
    iface = get_if()
    for i in range (0, 5000):
        srcport = random.randint(4000,5000)
        dstport = random.randint(4000,5000)
        n = random.randint(54,500)
        print ("sending on interface %s to %s" % (iface, str(addr)))
        pkt =  Ether(src=get_if_hwaddr(iface),dst = "00:00:0a:00:01:02")
        pkt = pkt /IP(dst=addr, tos=int(sys.argv[3]), flags=1, proto=6)
        pkt = pkt /TCP(sport = srcport, dport= dstport)
        myString = "z"*(n - 40)
        pkt = pkt/myString
        pkt.show2()
        sendp(pkt, iface=iface, verbose=False)
        time.sleep(1/int(sys.argv[4]))


def main():

    if(len(sys.argv) != 5):
        print('pass 4 arguments: <Number of Hosts> <IP Addresses> <TOS> <Number of Packets per Second>')
        exit(1)
    listOfNumbers = list(sys.argv[2].split(','))
    if(len(listOfNumbers) != int(sys.argv[1])):
        print("The Number of Hosts and IP Addresses don't match")
        exit(1)

    list_send = []
    for i in (listOfNumbers):
        addr = socket.gethostbyname(i)
        t1 = threading.Thread(target=sendpackets, args=(addr,))
        list_send.append(t1)

    for j in list_send:
        j.start()

    for j in list_send:
        j.join()

    exit(1)





if __name__ == '__main__':
    main()
