import socket

# create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()

# set port number
port = 9999

# connect to the server
client_socket.connect((host, port))

# read input from file
with open('input.txt', 'r') as f:
    lines = f.readlines()

# send messages to server
for line in lines:
    message = line.strip()
    client_socket.sendall(message.encode('utf-8'))
    # receive message from server
    data = client_socket.recv(1024).decode('utf-8')
    print(f"Received from server: {data}")

# close socket connection
client_socket.close()
