import os
import socket
import threading
from datetime import datetime
from exporter import Exporter

class LocalScanner:
    def __init__(self, base_ip, max_ips):
        self.base_ip = base_ip
        self.max_ips = max_ips
        self.active_ips = []
        self.open_ports_per_ip = {}
        self.port_range = range(20, 101)  # ports à tester

    def ping(self, ip):
        response = os.system(f"ping -n 1 -w 300 {ip} > nul")
        if response == 0:
            print(f"[✔] {ip} est actif")
            self.active_ips.append(ip)

    def scan_port(self, ip, port):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.3)
                result = s.connect_ex((ip, port))
                if result == 0:
                    if ip not in self.open_ports_per_ip:
                        self.open_ports_per_ip[ip] = []
                    self.open_ports_per_ip[ip].append(port)
        except:
            pass

    def scan_ports_on_active_ips(self):
        print("\n🔎 Scan des ports pour les IPs actives...")
        for ip in self.active_ips:
            print(f"\n🧪 Ports ouverts pour {ip} :")
            for port in self.port_range:
                self.scan_port(ip, port)

    def run(self):
        print(f"\n📡 Scan du réseau local : {self.base_ip}.0/24 (max {self.max_ips} IPs)")
        threads = []
        for i in range(1, self.max_ips + 1):
            ip = f"{self.base_ip}.{i}"
            t = threading.Thread(target=self.ping, args=(ip,))
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

        # Afficher les IPs détectées
        print("\n📦 Appareils détectés sur le réseau :")
        for ip in self.active_ips:
            print(f"🔸 {ip}")

        self.scan_ports_on_active_ips()

        # Sauvegarde automatique
        exporter = Exporter()
        exporter.export_local_scan(self.active_ips, self.open_ports_per_ip)
