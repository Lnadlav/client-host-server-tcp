import socket

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 12345))

    # Envoi d'une chaîne de caractères ASCII au serveur
    message = "Hello, server! This is ASCII data."
    client_socket.sendall(message.encode('utf-8'))

    # Attend la réponse du serveur
    data = client_socket.recv(1024)
    decoded_data = data.decode('utf-8')
    print(f"Message reçu du serveur (ASCII) : {decoded_data}")

    client_socket.close()

if __name__ == "__main__":
    start_client()

