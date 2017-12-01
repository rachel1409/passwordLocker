import socket
import os
import no_bytecode
from server import *

def login(client,loginstatus):
    client.send("Login\n")
    root_dir = os.getcwd()
    file_name = 'data.txt'
    file_path = os.path.join(root_dir, file_name)
    #isEmpty = os.stat(file_name).st_size == 0

    if os.path.exists(file_path):#and not isEmpty:
        data_file = open(file_name, 'r')
        while True:
            client.send("Enter your username:")
            username = str(client.recv(1024))
            
            client.send("Enter your password:")
            password = str(client.recv(1024))
            
            account = username + ", " + password

#there is a bug here preventing a successful login after a failed login

            if account in data_file.read():
                client.send("You are logged in!\n\n")
                loginstatus = True
                os.chdir('%s' % username)
                break
            else:
                client.send("Incorrect username or password. Try again.\n")
    else:
        client.send("No accounts have been made yet. Try creating an account.\n")
    return loginstatus
