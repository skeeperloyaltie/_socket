import socket

host = "127.0.0.1"
port = 12345

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_socket.bind((host, port))

# Listen for incoming connections
server_socket.listen()

print("Server listening on {}:{}".format(host, port))

# Wait for a client to connect
client_socket, addr = server_socket.accept()
print("Connected by", addr)

# Receive data from the client
while True:
    data = client_socket.recv(1024)
    if not data:
        break
    print("Received:", data.decode())

    # Send the same data back to the client
    client_socket.sendall(data)

# Close the connection
client_socket.close()
