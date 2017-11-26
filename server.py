import socket
import sys
from CreateAccount import *
from Login import *
import no_bytecode

def connect():
    host = "127.0.0.1"
    port = 7777

    return host, port

def error_check(server, host, port):
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((host, port))
    server.listen(5)

if __name__ == '__main__':
    server = socket.socket()
    host, port = connect()

    print "Starting server"
    print "Awaiting connection..."

    error_check(server, host, port)
    client, address = server.accept()
    client_connected = client.recv(1024)

    if client_connected == "Client connecting":
        print "\n"+"Client connected"
        client.send("Connection established"+"\n")

        while True:

            client.send("Press 1 to create an account\nPress 2 to login\nPress 3 to exit")
            response = client.recv(1024)

            if response == '1':
                create_account(client)

            elif response == '2':
                login(client)

            elif response == '3':
                shutdown = "Goodbye"
                client.send(shutdown)
                print "Server now closing"
                sys.exit()

            else:
                client.send("Choose a vaild option.\n")
    client.close()
