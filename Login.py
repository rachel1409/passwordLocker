import socket
import os
import csv
import hashlib
import no_bytecode
from rsa import *
from aes import *
from server import *

def login(client,loginstatus, key, clientkey):
    client.send(rsaencrypt("Login\n", clientkey))
    root_dir = os.getcwd()
    file_name = 'data.csv'
    file_path = os.path.join(root_dir, file_name)
    data = {}
    #isEmpty = os.stat(file_name).st_size == 0

    if os.path.exists(file_path):#and not isEmpty:
        with open(file_name, 'r') as f:
            reader = csv.reader(file_name)
            for row in reader:
                data[aesdecyrpt(row[0], gen_key())] = [row[1], row[2]]

        while True:
            client.send(rsaencrypt("Enter your username:", clientkey))
            username = rsadecrypt(client.recv(1024), key)
            
            client.send(rsaencrypt("Enter your password:", clientkey))
            password = rsadecrypt(client.recv(1024), key)
            
            #account = username + ", " + password

#there is a bug here preventing a successful login after a failed login
#** the data dictionary should fix this bug

            if username in data:
                if username in line[0]:
                    info = data[username]
                    h = hashlib.sha256()
                    h.update(password+aesdecrypt(info[1], gen_key()))
                    if h.hexdigest() == aesdecrypt(info[0], gen_key()):
                        client.send(rsaencrypt("You are logged in!\n\n", clientkey))
                        loginstatus = True
                        os.chdir('%s' % username)
                        break
                    else:
                        client.send(rsaencrypt("Incorrect username or password. Try again.\n", clientkey))
            else:
                client.send(rsaencrypt("Incorrect username or password. Try again.\n", clientkey))
    else:
        client.send(rsaencrypt("No accounts have been made yet. Try creating an account.\n", clientkey))
    return loginstatus
