import socket
import sys

# create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.sock)

# connect the socket to the server's address and port
server_address = ('localhost', 1234)
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)

# send data to the server
message = 'This is the message. It will be echoed.'
print('sending {!r}'.format(message))
sock.sendall(message.encode())

# receive data from the server
data = sock.recv(1024)
print('received {!r}'.format(data))

# send more data to the server
message = 'This is another message. It will also be echoed.'
print('sending {!r}'.format(message))
sock.sendall(message.encode())

# receive more data from the server
data = sock.recv(1024)
print('received {!r}'.format(data))

# close the socket
sock.close()
