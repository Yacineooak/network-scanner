import requests

class HTTPBannerScanner:
    def __init__(self, target, port):
        self.target = target
        self.port = port

    def scan(self):
        try:
            # Construction de l’URL
            protocol = "https" if self.port == 443 else "http"
            url = f"{protocol}://{self.target}:{self.port}"

            print(f"\n🌐 Récupération des headers HTTP sur : {url}")

            # Requête GET (on n’a pas besoin du corps de réponse)
            response = requests.get(url, timeout=3)

            # Affichage des headers
            print("📦 Headers reçus :")
            for header, value in response.headers.items():
                print(f"   {header}: {value}")

            # Analyse rapide
            if "Server" in response.headers:
                print(f"\n🧠 Serveur détecté : {response.headers['Server']}")

            if "X-Powered-By" in response.headers:
                print(f"🛠️ Technologie utilisée : {response.headers['X-Powered-By']}")

        except requests.exceptions.RequestException as e:
            print(f"❌ Erreur lors de la requête : {e}")
