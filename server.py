import socket
import sys
from ClearScreen import *
from CreateAccount import *
from Login import *
from PasswordManager import *
from rsa import *
from PLcrypto import *
import no_bytecode
import random

def connect():
    host = "127.0.0.1"
    port = 7777

    return host, port

def error_check(server, host, port):
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((host, port))
    server.listen(5)

def checkVerification(client, message):
    if not message:
        client.shutdown(socket.SHUT_RDWR)
        client.close()
        sys.exit(1)
    else:
        return message

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
        pubkeyfile = 'server.pem'
        key = gen_privkey()
        save_pubkey(pubkeyfile, gen_pubkey(key))
        aeskey = gen_key()

        client.send(pubkeyfile)
        clientkey = get_pubkey(client.recv(1024))
        client.send(rsaencrypt(aeskey, clientkey))
        nonce = random.random()
        client.send(PLencrypt(str(nonce), key, aeskey))
        if checkVerification(client, PLdecrypt(client.recv(1024), clientkey, aeskey)) == str(nonce-1):
            message = ""
            loginstatus = False

            while True:
                if loginstatus == True:
                    client.send(PLencrypt(message+"Press: \n- 1 to log out\n- 2 to manage passwords\n- 3 to exit", key, aeskey))
                    response = checkVerification(client, PLdecrypt(client.recv(1024), clientkey, aeskey))
                    
                    if response == '1':
                        loginstatus = False
                        os.chdir("..")
                        clearscrn()
                        message = "You are logged out\n"
                        
                    elif response == '2':
                        clearscrn()
                        manage_pass(client, key, clientkey, aeskey)
                        
                    elif response == '3':
                        clearscrn()
                        shutdown = "Goodbye"
                        client.send(PLencrypt(shutdown, key, aeskey))
                        print "Server now closing\n"
                        client.shutdown(socket.SHUT_RDWR)
                        client.close()
                        sys.exit()
                    else:
                        clearscrn()
                        message = "Choose a vaild option.\n"
                    clearscrn()

                elif loginstatus == False:
                    client.send(PLencrypt(message+"Press:\n- 1 to create an account\n- 2 to login\n- 3 to exit", key, aeskey))
                    response = checkVerification(client, PLdecrypt(client.recv(1024), clientkey, aeskey))
                    if response == '1':
                        clearscrn()
                        message = create_account(client, key, clientkey, aeskey)
                    
                    elif response == '2':
                        clearscrn()
                        loginstatus, message = login(client,loginstatus, key, clientkey, aeskey)
                        
                    elif response == '3':
                        clearscrn()
                        shutdown = "Goodbye"
                        client.send(PLencrypt(shutdown, key, aeskey))
                        print "Server now closing"
                        sys.exit()
                    else:
                        clearscrn()
                        message = "Choose a valid option.\n"
                    clearscrn()
        else:
            print "Key exchange failed\n"
            client.shutdown(socket.SHUT_RDWR)
            client.close()
            sys.exit(1)

    client.shutdown(socket.SHUT_RDWR)
    client.close()
