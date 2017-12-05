import socket
import sys
from CreateAccount import *
from Login import *
from PasswordManager import *
from rsa import *
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
        pubkeyfile = 'server.pem'
        key = gen_privkey()
        save_pubkey(pubkeyfile, gen_pubkey(key))

        client.send(pubkeyfile)
        clientkey = get_pubkey(client.recv(1024))

        loginstatus = False

        while True:
            if loginstatus == True:
                client.send(rsaencrypt("Press: \n- 1 to create account\n- 2 to log out\n- 3 to manage passwords\n- 4 to exit", clientkey))
                response = rsadecrypt(client.recv(1024), key)
                
                if response == '1':
                    create_account(client, key, clientkey)
                
                elif response == '2':
                    loginstatus = False
                    os.chdir("..")
                    
                elif response == '3':
                    manage_pass(client, key, clientkey)
                    
                elif response == '4':
                    shutdown = "Goodbye"
                    client.send(rsaencrypt(shutdown, clientkey))
                    print "Server now closing"
                    sys.exit()
                    
                else:
                    client.send(rsaencrypt("Choose a vaild option.\n", clientkey))

            elif loginstatus == False:
                client.send(rsaencrypt("Press:\n- 1 to create an account\n- 2 to login\n- 3 to exit", clientkey))
                response = rsadecrypt(client.recv(1024), key)
                if response == '1':
                    create_account(client, key, clientkey)
                
                elif response == '2':
                    loginstatus = login(client,loginstatus, key, clientkey)
                    
                elif response == '3':
                    shutdown = "Goodbye"
                    client.send(rsaencrypt(shutdown, clientkey))
                    print "Server now closing"
                    sys.exit()
                else:
                    client.send(rsaencrypt("Choose a valid option.\n", clientkey))
    client.close()
