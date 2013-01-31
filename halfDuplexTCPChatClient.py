"""
halfDuplexTCPChatClient.py
Mayank Gureja
01/25/2013
ECEC 433
"""

import socket
import sys


def main():
    """
    Main - Checks for correct input arguments and runs the appropriate methods
    """

    Client()


def Client():
    """
    Client - Runs the Half Duplex Chat Client
    """

    host = 'localhost'
    port = 22222
    ClientMessage = ""
    ServerMessage = ""

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client.connect((host, port))
    except:
        print "Cannot connect to server. Server may be down/ \nExiting..."
        sys.exit()

    while ClientMessage != "quit()" and ServerMessage != "quit()":
        ClientMessage = raw_input("Client: ")
        if ClientMessage != "quit()":
            client.send(ClientMessage)
            ServerMessage = client.recv(1024)
            print "Server: %s" % (ServerMessage)
        else:
            client.send(ClientMessage)
            client.close()


if __name__ == '__main__':
    main()
