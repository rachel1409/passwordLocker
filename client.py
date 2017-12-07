import socket
import sys
from rsa import *
from PLcrypto import *
import no_bytecode
import threading

def connect(server):
    host = "127.0.0.1"
    port = 7777
    server.connect((host, port))
    server.sendall("Client connecting")

def recv():
    response = rsadecrypt(server.recv(1024), key)
    if response == "Goodbye":
        server.close()
        sys.exit()
    else:
        while True:
            print response
            data = raw_input()
            
            if data:
                server.sendall(rsaencrypt(data, serverkey))
                break

def checkVerification(server, message):
    if not message:
        server.shutdown(socket.SHUT_RDWR)
        server.close()
        sys.exit(1)
    else:
        return message

if __name__ == '__main__':
    server = socket.socket()
    connect(server)

    pubkeyfile = 'client.pem'
    key = gen_privkey()
    save_pubkey(pubkeyfile, gen_pubkey(key))
    serverkey = get_pubkey(str(server.recv(1024)))
    server.sendall(pubkeyfile)
    aeskey = rsadecrypt(server.recv(1024), key)
    if not aeskey:
        sys.exit(1)
    if checkVerification(server, PLdecrypt(server.recv(1024), serverkey, aeskey)):
        server.sendall(PLencrypt("key received", key, aeskey))

        while True:
            #switch this on and removing everything below it will fix the bug where we cant send multiple messages to the client.
            #When it errors out, it spams a ton of text for about a minute so lets debug the rest of the program before we tackle the threading issue

            #threading.Thread(target=recv).start() 
            
            response = checkVerification(server, PLdecrypt(server.recv(1024), serverkey, aeskey))

            if response == "Goodbye":
                server.shutdown(socket.SHUT_RDWR)
                server.close()
                sys.exit()
            else:
                while True:
                    print response
                    data = raw_input()
                    
                    if data:
                        server.sendall(PLencrypt(data, key, aeskey))
                        break
