import socket
import threading
import time
from exporter import Exporter
from cve_checker import CVEChecker
from logger import setup_logger

logger = setup_logger("tcp_scanner")

class TCPScanner:
    def __init__(self, target, start_port, end_port):
        self.target = target
        self.start_port = start_port
        self.end_port = end_port
        self.open_ports = []
        self.exporter = Exporter()
        self.cve_checker = CVEChecker()

    def scan_port(self, port):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.5)
                result = s.connect_ex((self.target, port))
                if result == 0:
                    try:
                        service = socket.getservbyport(port)
                    except:
                        service = "inconnu"

                    port_info = {
                        "port": port,
                        "service": service.upper(),
                        "banner": "",
                        "cve": []
                    }

                    msg = f"[+] Port {port} ({service.upper()}) est OUVERT"
                    print(msg)
                    logger.info(msg)

                    # Banner grabbing
                    try:
                        s.sendall(b"Hello\r\n")
                        banner = s.recv(1024).decode(errors="ignore").strip()
                        if banner:
                            port_info["banner"] = banner
                            print(f"    \U0001F4E2 Bannière : {banner}")
                            logger.info(f"Bannière détectée sur le port {port} : {banner}")
                    except:
                        logger.debug(f"Impossible de récupérer la bannière sur le port {port}")
                        pass

                    # Alerte sécurité
                    vulnerable_ports = {
                        21: "FTP (non sécurisé)",
                        23: "Telnet (non chiffré)",
                        80: "HTTP (Port HTTP vulnerable)",
                        139: "NetBIOS (partage vulnérable)",
                        443: "HTTPS (Port HTTPS vulnerable)",
                        445: "SMB (cible de ransomwares)",
                        3389: "RDP (prise de contrôle à distance)",
                    }
                    if port in vulnerable_ports:
                        alert = f"⚠️  Alerte Sécurité : {vulnerable_ports[port]}"
                        print(f"   {alert}")
                        logger.warning(f"Port {port} : {vulnerable_ports[port]}")

                    # Recherche CVE
                    logger.info(f"🔍 Recherche de vulnérabilités CVE pour : {service}...")
                    cves = self.cve_checker.search_cve(service)
                    for cve in cves:
                        logger.warning(f"🛑 {cve}")
                    port_info["cve"] = cves

                    self.open_ports.append(port_info)
        except Exception as e:
            logger.error(f"[!] Erreur sur le port {port} : {e}")
            print(f"[!] Erreur sur le port {port} : {e}")

    def run(self):
        print(f"\n🔍 Scan TCP de {self.target} de {self.start_port} à {self.end_port}...\n")
        logger.info(f"Démarrage du scan TCP sur {self.target} de {self.start_port} à {self.end_port}")

        threads = []
        for port in range(self.start_port, self.end_port + 1):
            t = threading.Thread(target=self.scan_port, args=(port,))
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

        print("\n✅ Scan TCP terminé.")
        logger.info(f"Scan TCP terminé pour {self.target}")
        self.exporter.export_results(self.target, "tcp", self.open_ports)
