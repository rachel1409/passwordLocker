import socket
import os
import sys
import hashlib
import csv
from PLcrypto import *
from aes import *
import os.path
from PasswordHandler import *
import no_bytecode
from ClearScreen import *

def checkVerification(client, message):
    if not message:
        client.shutdown(socket.SHUT_RDWR)
        client.close()
        sys.exit(1)
    else:
        return message

def create_account(client, key, clientkey, aeskey):
    file_name = 'data.csv'
    unames = []
    umessage = ""
    pmessage = ""
    retval = "The account could not be created\n"
    if not os.path.isfile(file_name):
        w = open(file_name, "w+")
        w.close()
    with open(file_name, "r") as read_file:
        reader = csv.reader(read_file)
        for row in reader:
            unames.append(aesdecrypt(row[0], enckey()))

    while True:
        client.send(PLencrypt(umessage+"Enter a username:", key, aeskey))
        username = checkVerification(client, PLdecrypt(client.recv(1024), clientkey, aeskey))

        
        if username not in unames:
            if username != "":
                while True:
                    client.send(PLencrypt(pmessage+"Password must contain:\n-a minimum of 24 characters\n-at least 1 uppercase letter\n-at least 1 lowercase letter\n-at least 1 number\n-at least 1 symbol\nEnter a password:", key, aeskey))
                    password = checkVerification(client, PLdecrypt(client.recv(1024), clientkey, aeskey))
                    if pw_check(password):
                        clearscrn()
                        retval = "Account created!\n"
                        break
                    else:
                        clearscrn()
                        pmessage = "Please enter a valid password.\n"
                    break
                else:
                    clearscrn()
                    pmessage = "Please enter a valid username.\n"
                break
            else:
                clearscrn()
                pmessage = "Username taken, try again.\n"
            break

           
    #get hash of password and store those variables instead of storing the password itself
    psSalt = os.urandom(256)
    psHash = hashlib.sha256()
    psHash.update(password+psSalt.encode('base-64'))

    directory = username
    if not os.path.exists(directory): #creates a directory named after the user that will act as the storage location for their passwords
        os.makedirs(directory)
    with open(file_name, "a") as f:
        writer = csv.writer(f)
        writer.writerow([aesencrypt(username, enckey(), gen_iv()), aesencrypt(psHash.hexdigest(), enckey(), gen_iv()), aesencrypt(psSalt.encode('base-64'), enckey(), gen_iv())])
    return retval





