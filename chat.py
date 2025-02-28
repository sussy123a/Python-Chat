import socket
import threading

HOST = '127.0.0.1'  # Server IP Address
PORT = 5555  # Port to connect to

# Function to receive messages from server
def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            print(message)
        except:
            print("[-] Connection to server lost.")
            client_socket.close()
            break

# Start the client
def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))
    
    receive_thread = threading.Thread(target=receive_messages, args=(client,))
    receive_thread.start()
    
    while True:
        message = input("")
        if message.lower() == "exit":
            client.close()
            break
        client.send(message.encode('utf-8'))

if __name__ == "__main__":
    start_client()
