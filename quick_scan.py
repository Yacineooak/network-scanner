import socket
import threading

top_ports = [
    20, 21, 22, 23, 25, 53, 67, 68, 69, 80,
    110, 111, 123, 135, 137, 138, 139, 143, 161, 162,
    179, 389, 443, 445, 465, 514, 515, 520, 587, 593,
    636, 993, 995, 1025, 1080, 1194, 1433, 1723, 3306, 3389,
    5060, 5900, 8080, 8443, 8888, 8880, 10000, 32768, 49152, 49153,
    49154, 49155, 49156, 49157, 49158, 49159, 49160, 49161, 49162, 49163,
    49164, 49165, 49166, 49167, 49168, 49169, 49170, 49171, 49172, 49173,
    49174, 49175, 49176, 49177, 49178, 49179, 49180, 49181, 49182, 49183,
    49184, 49185, 49186, 49187, 49188, 49189, 49190, 49191, 49192, 49193,
    49194, 49195, 49196, 49197, 49198, 49199, 49200, 49201, 49202, 49203
]

class QuickScanner:
    def __init__(self, target):
        self.target = target
        self.open_ports = []
        self.lock = threading.Lock()

    def scan_port(self, port):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.5)
                result = s.connect_ex((self.target, port))
                if result == 0:
                    with self.lock:
                        self.open_ports.append(port)
        except:
            pass

    def run(self):
        print(f"\n⚡ Scan rapide des 100 ports les plus utilisés sur {self.target}...\n")
        threads = []
        for port in top_ports[:100]:
            t = threading.Thread(target=self.scan_port, args=(port,))
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

        for port in sorted(self.open_ports):
            try:
                service = socket.getservbyport(port)
            except:
                service = "Inconnu"
            print(f"[+] Port {port} ({service.upper()}) est OUVERT")

        print("\n✅ Scan rapide terminé.")
