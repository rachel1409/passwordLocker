import socket
import os
import hashlib
import csv
from rsa import *
from aes import *
import os.path
from PasswordHandler import *
import no_bytecode

def create_account(client, key, clientkey):
    file_name = 'data.csv'
    unames = []

    if not os.path.isfile(file_name):
        w = open(file_name, "w+")
        w.close()
    with open(file_name, "r") as read_file:
        reader = csv.reader(read_file)
        for row in reader:
            unames.append(aesdecrypt(row[0], gen_key()))

    while True:
        client.send(rsaencrypt("Enter a username:", clientkey))
        username = rsadecrypt(client.recv(1024), key)

        if username not in unames:
            if username != "":
                while True:
                    #client.send(rsaencrypt("Password must contain a minimum of 24 character.\n", clientkey))
                    #client.send(rsaencrypt("Password must contain:\n", clientkey))
                    #client.send(rsaencrypt("-1 uppercase letter\n-1 lowercase letter\n-1 number\n-1 symbol\n", clientkey))
                    client.send(rsaencrypt("Enter a password:", clientkey))
                    password = rsadecrypt(client.recv(1024), key)

                    if pw_check(password):
                        client.send(rsaencrypt("Account created!\n", clientkey))
                        break
                    else:
                        client.send(rsaencrypt("Please enter a valid password.\n", clientkey))
                break
            else:
                client.send(rsaencrypt("Please enter a valid username.\n", clientkey))
        else:
            client.send(rsaencrypt("Username taken, try again.\n", clientkey))

           
    #get hash of password and store those variables instead of storing the password itself
    psSalt = os.urandom(256)
    psHash = hashlib.sha256()
    psHash.update(password+psSalt.encode('base-64'))

    directory = username
    if not os.path.exists(directory): #creates a directory named after the user that will act as the storage location for their passwords
        os.makedirs(directory)
    with open(file_name, "a") as file_name:
        writer = csv.writer(file_name)
        writer.writerow([aesencrypt(username, gen_key(), gen_iv()), aesencrypt(psHash.hexdigest(), gen_key(), gen_iv()), aesencrypt(psSalt.encode('base-64'), gen_key(), gen_iv())])





