import requests
from urllib.parse import urlparse

class BannerScanner:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def scan(self):
        protocol = "https" if self.port == 443 else "http"
        url = f"{protocol}://{self.ip}:{self.port}"
        print(f"\n🌐 Récupération des headers HTTP sur : {url}")

        try:
            response = requests.get(url, timeout=5)
            print("📦 Headers reçus :")
            for key, value in response.headers.items():
                print(f"   {key}: {value}")

            server = response.headers.get("Server", "Inconnu")
            print(f"\n🧠 Serveur détecté : {server}")
        except requests.exceptions.RequestException as e:
            print(f"[❌] Erreur lors de la connexion à {url} : {e}")
