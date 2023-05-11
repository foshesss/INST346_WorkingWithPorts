import socket

def main():
    port = 9001
    host = "localhost"

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print(f"Listening on port {port}...")

    while True:
        print("Server still open")

    server_socket.close()

if __name__ == '__main__':
    main()
