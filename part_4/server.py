import socket

host = "127.0.0.1"
port = 12345

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to a specific address and port
server_socket.bind((host, port))

print("Server listening on {}:{}".format(host, port))

# Receive data from the client and send it back
while True:
    data, addr = server_socket.recvfrom(1024)
    print("Received from client:", data.decode())
    server_socket.sendto(data, addr)
