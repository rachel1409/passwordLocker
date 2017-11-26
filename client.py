import socket
import sys
import no_bytecode

def connect(server):
    host = "127.0.0.1"
    port = 7777
    server.connect((host, port))
    server.sendall("Client connecting")


if __name__ == '__main__':
    server = socket.socket()
    connect(server)

    while True:
        response = server.recv(1024)
        if response == "Goodbye":

            server.close()
            sys.exit()
        else:
            while True:
                print response
                data = raw_input()

                if data:
                    server.sendall(data)
                    break
