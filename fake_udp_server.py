import socket

def start_fake_udp_server(host='127.0.0.1', port=9999):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((host, port))
    print(f"🟢 Serveur UDP en écoute sur {host}:{port}...")

    while True:
        data, addr = sock.recvfrom(1024)
        print(f"[📨] Reçu de {addr} : {data.decode(errors='ignore')}")
        sock.sendto("Reponse du serveur UDP".encode("utf-8"), addr)

if __name__ == "__main__":
    start_fake_udp_server()
