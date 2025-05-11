import subprocess
import platform

class OSDetector:
    def __init__(self, target):
        self.target = target

    def detect_os(self):
        try:
            if platform.system().lower() == "windows":
                command = ["ping", "-n", "1", self.target]
            else:
                command = ["ping", "-c", "1", self.target]

            result = subprocess.run(command, capture_output=True, text=True)
            output = result.stdout

            for line in output.splitlines():
                if "TTL=" in line.upper():
                    ttl_part = line.upper().split("TTL=")[-1]
                    ttl = int(ttl_part.split()[0])
                    return self.guess_os(ttl)

        except Exception as e:
            return f"❌ Erreur lors de la détection OS : {e}"

        return "⛔ Impossible de détecter le TTL."

    def guess_os(self, ttl):
        if ttl >= 128:
            return f"🪟 Système probable : Windows (TTL={ttl})"
        elif ttl >= 64:
            return f"🐧 Système probable : Linux/Unix (TTL={ttl})"
        elif ttl >= 255:
            return f"📡 Système probable : Cisco/Routeur (TTL={ttl})"
        else:
            return f"❓ OS inconnu (TTL={ttl})"
