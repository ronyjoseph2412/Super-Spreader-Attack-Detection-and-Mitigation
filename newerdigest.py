import nnpy
import struct
import ipaddress
from p4utils.utils.topology import Topology
from p4utils.utils.sswitch_API import SimpleSwitchAPI
import threading

class DigestController():

    def __init__(self, sw_name):
        self.sw_name = sw_name
        self.topo = Topology(db="topology.db")
        self.sw_name = sw_name
        self.thrift_port = self.topo.get_thrift_port(sw_name)
        self.controller = SimpleSwitchAPI(self.thrift_port)
        self.ip_dict = {}
        print("Activated",sw_name)

    def store_ip(self, src_ip, dst_ip):
        print(self.ip_dict)
        if src_ip in self.ip_dict:
            found = False
            for i, ip_data in enumerate(self.ip_dict[src_ip]):
                if ip_data[0] == dst_ip:
                    self.ip_dict[src_ip][i][1] += 1
                    found = True
                    break
            if not found:
                self.ip_dict[src_ip].append([dst_ip, 1])
        else:
            self.ip_dict[src_ip] = [[dst_ip, 1]]

    def super_spreader_detector(self):
        threshold = 200  # adjust the threshold according to your network
        for src_ip, dst_ips in self.ip_dict.items():
            for dst_ip, packet_count in dst_ips:
                if len(dst_ips) > 2 and packet_count > threshold:
                    print("Super spreader detected! Src IP: ",src_ip, " Dst IP: ",dst_ips," Packet Count: ",packet_count)

    def recv_msg_digest(self, msg):
        topic, device_id, ctx_id, list_id, buffer_id, num = struct.unpack("<iQiiQi", msg[:32])
        offset = 9
        msg = msg[32:]
        for sub_message in range(num):
            random_num, src, dst = struct.unpack("!BII", msg[0:offset])
            self.store_ip(str(ipaddress.IPv4Address(src)), str(ipaddress.IPv4Address(dst)))
            msg = msg[offset:]
        self.controller.client.bm_learning_ack_buffer(ctx_id, list_id, buffer_id)
        self.super_spreader_detector()

    def run_digest_loop(self):
        sub = nnpy.Socket(nnpy.AF_SP, nnpy.SUB)
        notifications_socket = self.controller.client.bm_mgmt_get_info().notifications_socket
        print("connecting to notification sub %s" % notifications_socket)
        sub.connect(notifications_socket)
        sub.setsockopt(nnpy.SUB, nnpy.SUB_SUBSCRIBE, '')

        while True:
            msg = sub.recv()
            self.recv_msg_digest(msg)


def main():
    controllers = [DigestController("s1"), DigestController("s2"), DigestController("s3")]
    threads = []
    for controller in controllers:
        thread = threading.Thread(target=controller.run_digest_loop)
        threads.append(thread)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
