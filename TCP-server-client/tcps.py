import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 12345))
    server_socket.listen(1)

    print("Le serveur attend une connexion...")

    while True:
        client_socket, addr = server_socket.accept()

        with client_socket:
            print(f"Connexion établie avec {addr}")

            while True:
                data = client_socket.recv(1024)
                if not data:
                    break
                decoded_data = data.decode('utf-8')
                print(f"Message reçu du client (ASCII) : {decoded_data}")

                # Convertit le message ASCII en majuscules et renvoie au client
                encoded_data = decoded_data.upper().encode('utf-8')
                client_socket.sendall(encoded_data)

if __name__ == "__main__":
    start_server()
