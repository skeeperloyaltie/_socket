import socket

def main():
    # Create a socket
    s_ck = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Connect to the server
    s_ck.connect(("localhost", 1234))

    # Send a msg to the server
    s_ck.sendall("Hello, world!".encode())

    # Receive a reply from the server
    msg = s_ck.recv(1024)

    # Print the reply
    print(msg.decode())

    # Close the connection
    s_ck.close()

if __name__ == "__main__":
    main()
