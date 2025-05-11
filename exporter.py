import os
import json
from datetime import datetime

class Exporter:
    def __init__(self):
        self.folder = "exports"
        if not os.path.exists(self.folder):
            os.makedirs(self.folder)

    def export_tcp_scan(self, target, results):
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        base_filename = f"{self.folder}/tcp_scan_{target}_{timestamp}"

        # Enregistrement en TXT
        with open(base_filename + ".txt", "w", encoding="utf-8") as f:
            for r in results:
                f.write(r + "\n")

        # Enregistrement en JSON
        with open(base_filename + ".json", "w", encoding="utf-8") as f:
            json.dump(results, f, indent=4)

        print("\n✅ Résultats TCP enregistrés.")

    def export_udp_scan(self, target, results):
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        base_filename = f"{self.folder}/udp_scan_{target}_{timestamp}"

        with open(base_filename + ".txt", "w", encoding="utf-8") as f:
            for r in results:
                f.write(r + "\n")

        with open(base_filename + ".json", "w", encoding="utf-8") as f:
            json.dump(results, f, indent=4)

        print("\n✅ Résultats UDP enregistrés.")

    def export_local_scan(self, active_ips, ports_open_per_ip):
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        base_filename = f"{self.folder}/local_scan_{timestamp}"

        # Export TXT
        with open(base_filename + ".txt", "w", encoding="utf-8") as f:
            for ip in active_ips:
                f.write(f"{ip}\n")
                if ip in ports_open_per_ip:
                    for port in ports_open_per_ip[ip]:
                        f.write(f"    Port ouvert : {port}\n")

        # Export JSON
        data = {
            "ips_detectees": active_ips,
            "ports_ouverts": ports_open_per_ip
        }
        with open(base_filename + ".json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

        print(f"\n✅ Résultats enregistrés dans :\n   📄 {base_filename}.txt\n   📄 {base_filename}.json")

    def export_results(self, target, scan_type, data):
        # Utilisé pour les scans enrichis ou scans multi IPs
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        base_filename = f"{self.folder}/{scan_type}_scan_{target}_{timestamp}"

        with open(base_filename + ".txt", "w", encoding="utf-8") as f:
            for item in data:
                f.write(f"Port : {item['port']} | Service : {item['service']}\n")
                if item.get("banner"):
                    f.write(f"  → Bannière : {item['banner']}\n")
                if item.get("cve"):
                    f.write(f"  → CVE : {', '.join(item['cve'])}\n")
                f.write("\n")

        with open(base_filename + ".json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

        print(f"\n✅ Résultats exportés dans :\n   📄 {base_filename}.txt\n   📄 {base_filename}.json")
