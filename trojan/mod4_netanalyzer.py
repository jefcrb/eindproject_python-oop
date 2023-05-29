from scapy.all import sniff
import os
import json


class NetworkAnalyzer:
    def __init__(self, host_id):
        self.log_file = os.path.join("..", "logs", host_id, "network", "network_traffic.json")
        self.stop_sniffing = False

    def process_packet(self, packet):
        data = {
            'time': str(packet.time),
            'src': str(packet[0][1].src),
            'dst': str(packet[0][1].dst),
            'proto': str(packet[0][1].proto)
        }
        with open(self.log_file, 'a') as f:
            json.dump(data, f)
            f.write('\n')

    def start(self):
        sniff(prn=self.process_packet, stop_filter=self.should_stop_sniffing)

    def stop(self):
        self.stop_sniffing = True

    def should_stop_sniffing(self, packet):
        return self.stop_sniffing
