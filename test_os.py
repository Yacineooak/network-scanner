from os_detector import OSDetector

target = input("Entrez l'adresse IP cible : ")
detector = OSDetector(target)
resultat = detector.detect_os()
print(resultat)
