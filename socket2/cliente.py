import socket
import sys
from urllib.parse import urlparse

def main():
    if len(sys.argv) != 2:
        print("Por favor, forneça a URL do servidor.")
        return

    server_url = sys.argv[1]
    parsed_url = urlparse(server_url)

    if not parsed_url.scheme or not parsed_url.netloc:
        print("Formato de URL inválido.")
        return

    server_address = parsed_url.hostname
    server_port = parsed_url.port

    if not server_port:
        server_port = 8088  # Porta padrão

    try:
        # Criando socket TCP/IP
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Conectando o socket ao servidor
        client_socket.connect((server_address, server_port))

        # Enviando a URL do arquivo ao servidor
        client_socket.sendall(parsed_url.path.encode())

        # Recebendo a resposta do servidor
        received_data = client_socket.recv(1024)

        print("Resposta do servidor:")
        print(received_data.decode())

    except Exception as e:
        print(f"Erro ao se conectar ao servidor: {e}")

    finally:
        # Fechando o socket
        client_socket.close()

if __name__ == "__main__":
    main()
