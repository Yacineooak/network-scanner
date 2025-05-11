from tcp_scanner import TCPScanner
from udp_scanner import UDPScanner
import os

class MultiIPScanner:
    def __init__(self, filepath, scan_type, start_port, end_port):
        self.filepath = filepath
        self.scan_type = scan_type.upper()
        self.start_port = start_port
        self.end_port = end_port

    def scan(self):
        if not os.path.exists(self.filepath):
            print(f"❌ Le fichier '{self.filepath}' n'existe pas.")
            return

        with open(self.filepath, 'r') as file:
            ips = file.read().splitlines()

        for ip in ips:
            print(f"\n🔍 Scan de {ip} en {self.scan_type} de {self.start_port} à {self.end_port}")
            if self.scan_type == "TCP":
                scanner = TCPScanner(ip, self.start_port, self.end_port)
                scanner.run()  # ✅ méthode correcte (OOP)
            elif self.scan_type == "UDP":
                scanner = UDPScanner(ip, self.start_port, self.end_port)
                scanner.run()  # ✅ méthode correcte (OOP)
            else:
                print(f"❌ Type de scan '{self.scan_type}' non reconnu.")
