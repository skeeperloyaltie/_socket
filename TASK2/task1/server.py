import socket

def main():
    # Create a socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to a port
    sock.bind(("localhost", 8080))

    # Listen for incoming connections
    sock.listen(1)

    # Accept an incoming connection
    connection, address = sock.accept()

    # Receive a message from the client
    message = connection.recv(1024)

    # Send a reply back to the client
    connection.sendall("Hello, world!".encode())

    # Close the connection
    connection.close()

if __name__ == "__main__":
    main()
