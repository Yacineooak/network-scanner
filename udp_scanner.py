import socket
import threading
from exporter import Exporter
from logger import setup_logger

logger = setup_logger()

class UDPScanner:
    def __init__(self, target, start_port, end_port):
        self.target = target
        self.start_port = start_port
        self.end_port = end_port
        self.open_ports = []
        self.exporter = Exporter()

    def scan_port(self, port):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
                s.settimeout(1)
                s.sendto(b"ping", (self.target, port))
                try:
                    data, _ = s.recvfrom(1024)
                    logger.info(f"[UDP] Port {port} est OUVERT (réponse : {data})")
                    print(f"[UDP] Port {port} est OUVERT")
                    self.open_ports.append(port)
                except socket.timeout:
                    logger.info(f"[UDP] Port {port} est OUVERT ou FILTRÉ (pas de réponse)")
                    print(f"[UDP] Port {port} est OUVERT ou FILTRÉ (pas de réponse)")
                    self.open_ports.append(port)
        except Exception as e:
            logger.error(f"[!] Erreur UDP sur le port {port} : {e}")

    def run(self):
        print(f"\n🔍 Scan UDP de {self.target} de {self.start_port} à {self.end_port}...\n")
        logger.info(f"Démarrage du scan UDP sur {self.target} de {self.start_port} à {self.end_port}")
        threads = []
        for port in range(self.start_port, self.end_port + 1):
            t = threading.Thread(target=self.scan_port, args=(port,))
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

        print("\n✅ Scan UDP terminé.")
        logger.info(f"Scan UDP terminé pour {self.target}")
        self.exporter.export_udp_scan(self.target, self.open_ports)
