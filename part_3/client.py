import socket

host = "127.0.0.1"
port = 12345

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((host, port))

# Send data to the server and receive it back
while True:
    message = input("Enter message to send to server: ")
    client_socket.sendall(message.encode())
    data = client_socket.recv(1024)
    print("Received from server:", data.decode())

# Close the connection
client_socket.close()
