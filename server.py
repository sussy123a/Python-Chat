import socket
import threading

# Server configuration
HOST = '127.0.0.1'  # Localhost
PORT = 5555  # Port to bind the server

# List to hold connected clients
clients = []

# Function to handle client messages
def handle_client(client_socket, client_address):
    print(f"[+] New connection from {client_address}")
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(f"[{client_address}] {message}")
            broadcast(message, client_socket)
        except:
            break
    print(f"[-] Connection closed from {client_address}")
    clients.remove(client_socket)
    client_socket.close()

# Function to broadcast messages to all clients
def broadcast(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message.encode('utf-8'))
            except:
                client.close()
                clients.remove(client)

# Start the server
def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)
    print(f"[*] Server started on {HOST}:{PORT}")
    
    while True:
        client_socket, client_address = server.accept()
        clients.append(client_socket)
        thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        thread.start()

if __name__ == "__main__":
    start_server()
