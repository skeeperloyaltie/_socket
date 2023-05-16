import socket

def main():
    # Create a socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    sock.connect(("localhost", 8080))

    # Send a message to the server
    sock.sendall("Hello, world!".encode())

    # Receive a reply from the server
    message = sock.recv(1024)

    # Print the reply
    print(message.decode())

    # Close the connection
    sock.close()

if __name__ == "__main__":
    main()
