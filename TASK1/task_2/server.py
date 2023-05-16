import socket

# create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()

# set port number
port = 9999

# bind the socket to a public host and port
server_socket.bind((host, port))

# set maximum connections
server_socket.listen(10)

while True:
    # wait for client connection
    client_socket, address = server_socket.accept()
    print(f"Connection from {address} has been established!")

    while True:
        # receive data from client
        data = client_socket.recv(1024).decode('utf-8')
        if not data:
            break

        print(f"Received from client: {data}")
        
        # send data back to client
        client_socket.sendall(data.encode('utf-8'))

    # close client socket
    client_socket.close()
