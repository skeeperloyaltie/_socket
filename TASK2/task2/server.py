import socket

def main():
    # Create a socket
    s_cc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to a port
    s_cc.bind(("localhost", 8080))

    # Listen for incoming connections
    s_cc.listen(1)

    # Accept an incoming con
    con, address = s_cc.accept()

    # Receive a msg from the client
    msg = con.recv(1024)

    # Send a reply back to the client
    con.sendall("Hello, world!".encode())

    # Close the con
    con.close()

if __name__ == "__main__":
    main()
