# syn_scanner.py
from scapy.all import IP, TCP, sr1, conf
import time

class SYNScanner:
    def __init__(self, target, ports):
        self.target = target
        self.ports = ports
        self.open_ports = []

    def scan(self):
        print(f"\n⚡ Scan SYN de {self.target}...")
        conf.verb = 0  # silence scapy
        for port in self.ports:
            pkt = IP(dst=self.target)/TCP(dport=port, flags="S")
            response = sr1(pkt, timeout=1, verbose=0)

            if response is None:
                print(f"[-] Port {port} : Pas de réponse")
            elif response.haslayer(TCP):
                if response[TCP].flags == 0x12:  # SYN-ACK
                    print(f"[+] Port {port} est OUVERT (SYN-ACK)")
                    self.open_ports.append(port)
                elif response[TCP].flags == 0x14:  # RST
                    print(f"[-] Port {port} est FERMÉ (RST)")
        print("\n✅ Scan SYN terminé.")
