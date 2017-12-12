import socket
import os
import sys
import csv
import hashlib
import no_bytecode
from aes import *
from PLcrypto import *
from server import *

# checks if signature was verified
def checkVerification(client, message):
    if not message: #shutdown connection
        client.shutdown(socket.SHUT_RDWR)
        client.close()
        sys.exit(1) #return an error
    else:
        return message

def login(client, loginstatus, key, clientkey, aeskey):
    root_dir = os.getcwd()
    file_name = 'data.csv'
    file_path = os.path.join(root_dir, file_name)
    data = {}
    #isEmpty = os.stat(file_name).st_size == 0

    if os.path.exists(file_path):
        message = ""
        retval = ""
        # read in all saved username/password pairs and store in dictionary
        # only decrypt the username for security reasons
        with open(file_name, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                data[aesdecrypt(row[0], enckey())] = [row[1], row[2]]

        while True:
            client.send(PLencrypt(message+"Enter your username:", key, aeskey))
            username = checkVerification(client, PLdecrypt(client.recv(1024), clientkey, aeskey))
            
            client.send(PLencrypt("Enter your password:", key, aeskey))
            password = checkVerification(client, PLdecrypt(client.recv(1024), clientkey, aeskey))

            # AMB - hash the given password with the stored salt and compare to stored password
            if username in data:
                info = data[username]
                h = hashlib.sha256()
                h.update(password+aesdecrypt(info[1], enckey()))
                if h.hexdigest() == aesdecrypt(info[0], enckey()):
                    clearscrn()
                    retval = "You are logged in!\n"
                    loginstatus = True
                    # change to user's directory
                    os.chdir('%s' % username)
                    break
                else:
                    clearscrn()
                    message = "Incorrect username or password. Try again.\n"
            else:
                clearscrn()
                message = "Incorrect username or password. Try again.\n"
    else:
        clearscrn()
        retval = "No accounts have been made yet. Try creating an account.\n"
    return loginstatus, retval
