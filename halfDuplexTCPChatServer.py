"""
halfDuplexTCPChatServer.py
Mayank Gureja
01/25/2013
ECEC 433
"""

import socket


def main():
    """
    Main - Checks for correct input arguments and runs the appropriate methods
    """

    Server()


def Server():
    """
    Server - Runs the Half Duplex Chat Server
    """

    host = 'localhost'
    port = 22222
    ClientMessage = ""
    ServerMessage = ""

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((host, port))
    server.listen(1)

    print "INFO: I am listening at %s" % (str(server.getsockname()))
    print "INFO: I am ready to chat with a new client!"

    conn, addr = server.accept()
    print "Connecting socket created between %s and %s" % (conn.getsockname(), conn.getpeername())

    while True:
        ClientMessage = conn.recv(1024)
        if ClientMessage != "quit()" and ServerMessage != "quit()":
            print "Client: %s" % (ClientMessage)
            ServerMessage = raw_input("Server: ")
            conn.send(ServerMessage)
        else:
            conn.send(ServerMessage)
            ServerMessage = ""
            print "I am ready to chat with a new client!"
            conn.close()
            conn, addr = server.accept()
            print "Connecting socket created between %s and %s" % (conn.getsockname(), conn.getpeername())


if __name__ == '__main__':
    main()
