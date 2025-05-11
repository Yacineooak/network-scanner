import nvdlib

class CVEChecker:
    def search_cve(self, service_name):
        print(f"\n🔍 Recherche de vulnérabilités CVE pour : {service_name}...")
        try:
            # on laisse la clé API vide si on en a pas
            results = nvdlib.searchCVE(keywordSearch=service_name, key=None)

            if not results:
                print("❌ Aucune CVE trouvée.")
                return

            for cve in results[:3]:
                print(f"🛑 {cve.id} - {cve.descriptions[0].value}")
        except Exception as e:
            print(f"❌ Erreur lors de la recherche CVE : {e}")
