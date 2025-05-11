from tcp_scanner import TCPScanner
from udp_scanner import UDPScanner
from local_scanner import LocalScanner
from os_detector import OSDetector
from firewall_detector import FirewallDetector
from quick_scan import QuickScanner
from syn_scanner import SYNScanner
from banner_scanner import BannerScanner
from multi_ip_scanner import MultiIPScanner

def menu():
    while True:
        print("\n=== Menu Principal ===")
        print("1. Scanner TCP")
        print("2. Scanner UDP")
        print("3. Scanner Réseau Local")
        print("4. Détection du système d'exploitation (OS)")
        print("5. Détection de ports filtrés (pare-feu)")
        print("6. Scan rapide (Top 100 ports)")
        print("7. Scan SYN (admin/root)")
        print("8. Scan de bannière HTTP")
        print("9. Scan multiple IPs (via fichier)")
        print("0. Quitter")

        choix = input("Choisissez une option (0-9) : ")

        if choix == "1":
            ip = input("Entrez l'adresse IP cible : ")
            start = int(input("Port de départ : "))
            end = int(input("Port de fin : "))
            scanner = TCPScanner(ip, start, end)
            scanner.run()

        elif choix == "2":
            ip = input("Entrez l'adresse IP cible : ")
            start = int(input("Port de départ : "))
            end = int(input("Port de fin : "))
            scanner = UDPScanner(ip, start, end)
            scanner.run()

        elif choix == "3":
            scanner = LocalScanner()
            scanner.run()

        elif choix == "4":
            ip = input("Entrez l'adresse IP cible : ")
            scanner = OSDetector(ip)
            scanner.run()  # ✅ On utilise run() pour uniformiser avec les autres classes


        elif choix == "5":
            ip = input("Entrez l'adresse IP cible : ")
            start = int(input("Port de départ : "))
            end = int(input("Port de fin : "))
            scanner = FirewallDetector(ip, start, end)
            scanner.run()  # ✅ run() au lieu de scan()


        elif choix == "6":
            ip = input("Entrez l'adresse IP ou nom de domaine : ")
            scanner = QuickScanner(ip)
            scanner.run()  # ✅

        elif choix == "7":
            ip = input("Entrez l'adresse IP ou nom de domaine : ")
            start = int(input("Port de départ : "))
            end = int(input("Port de fin : "))
            scanner = SYNScanner(ip, start, end)
            scanner.run()  # ✅

        elif choix == "8":
            ip = input("Entrez l'adresse IP ou nom de domaine : ")
            port = input("Port HTTP (80 ou 443) : ")
            scanner = BannerScanner(ip, port)
            scanner.run()  # ✅

        elif choix == "9":
            print("\n=== Scan de plusieurs IPs ===")
            filename = input("📄 Nom du fichier contenant les IPs : ")
            scan_type = input("🌐 Type de scan (TCP ou UDP) : ")
            start_port = int(input("Port de départ : "))
            end_port = int(input("Port de fin : "))

            scanner = MultiIPScanner(filename, scan_type, start_port, end_port)
            scanner.run()  # ✅


        elif choix == "0":
            print("👋 Au revoir !")
            break

        else:
            print("❌ Option invalide. Réessayez.")

if __name__ == "__main__":
    menu()
