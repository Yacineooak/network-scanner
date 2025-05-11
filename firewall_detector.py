import socket
import time

class FirewallDetector:
    def __init__(self, target, ports):
        self.target = target
        self.ports = ports
        self.filtered_ports = []

    def detect(self):
        print(f"\n🛡️ Détection de ports filtrés sur {self.target}...\n")
        for port in self.ports:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(2)
                start = time.time()
                result = s.connect_ex((self.target, port))
                duration = time.time() - start
                s.close()

                if result != 0 and duration >= 2:
                    print(f"[🔒] Port {port} POTENTIELLEMENT FILTRÉ (timeout)")
                    self.filtered_ports.append(port)

            except Exception as e:
                print(f"Erreur sur le port {port} : {e}")

        return self.filtered_ports
