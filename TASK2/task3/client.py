import socket

# Create a client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect(("127.0.0.1", 1345))

# Send a message to the server
client_socket.sendall("Hello, server!".encode())

# Receive a message from the server
message = client_socket.recv(1024).decode()

# Print the message
print(message)

# Close the client socket
client_socket.close()
