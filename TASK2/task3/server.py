import socket

# Create a server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the server socket to port 8080
server_socket.bind(("127.0.0.1", 1345))

# Listen for connections
server_socket.listen()

while True:
    # Accept a connection from a client
    client_socket, client_address = server_socket.accept()

    # Get the client's message
    message = client_socket.recv(1024).decode()
    print('Connection received.')

    # Convert the message to a bytes object
    message = message.encode("utf-8")

    # Send a message back to the client
    client_socket.sendall(message)

    # Close the client socket
    client_socket.close()
