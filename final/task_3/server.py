import socket
import sys

# create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind the socket to a specific address and port
server_address = ('localhost', 1234)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

# listen for incoming connections
sock.listen(1)

def handle_client_connection(client_socket):
    while True:
        # receive data from the client
        data = client_socket.recv(1024)
        print('received {!r}'.format(data))
        if data:
            # send the same data back to the client
            client_socket.sendall(data)
        else:
            # no more data from the client
            print('no data from', client_address)
            break

# wait for a connection
print('waiting for a connection')
connection, client_address = sock.accept()
print('connection from', client_address)

# handle the first client connection
handle_client_connection(connection)

# start 10 other clients in the background from a file
for i in range(1, 11):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 1234))
    client_socket.sendall(('client ' + str(i)).encode())
    client_socket.close()

# close the server socket
sock.close()
