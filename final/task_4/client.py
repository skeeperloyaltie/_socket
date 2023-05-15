import socket

host = "localhost"
port = 1234

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Send data to the server and receive it back
while True:
    message = input("Enter message to send to server: ")
    client_socket.sendto(message.encode(), (host, port))
    data, addr = client_socket.recvfrom(1024)
    # print("Received from server:", data.decode())
