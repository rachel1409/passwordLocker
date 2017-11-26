import socket
import os
import os.path
from PasswordHandler import *
import no_bytecode

def create_account(client):
    file_name = 'data.txt'

    data_file = open(file_name, 'a+')
    read_file = open(file_name, 'r')

    while True:
        client.send("Enter a username:")
        username = str(client.recv(1024))

        if username not in read_file.read():
            if username != "":
                while True:
                    client.send("Enter a password:")
                    password = str(client.recv(1024))

                    if pw_check(password):
                        client.send("Account created!\n\n")
                        break
                    else:
                        client.send("Please enter a valid password.\n")
                break
            else:
                client.send("Please enter a valid username.\n")
        else:
            client.send("Username taken, try again.\n")

    data_file.write(username + ", " + password + "\n")
    data_file.close()
