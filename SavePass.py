import socket
import os
import os.path
import csv
from rsa import *
from aes import *
import no_bytecode

def save_pass(client, key, clientkey):
  client.send(rsaencrypt("Enter a name for this entry:", clientkey))
  entry = rsadecrypt(client.recv(1024), key)
  client.send(rsaencrypt("Enter a username:", clientkey))
  username = rsadecrypt(client.recv(1024), key)
  client.send(rsaencrypt("Enter a password:", clientkey))
  password = rsadecrypt(client.recv(1024), key)

  #Convert username and password to encrypted data here and replace variables below with encrypted variables        

  with open("%s.csv" % entry,"w+") as f:
    writer = csv.writer(f)
    writer.writerow([aesencrypt(username, gen_key(), gen_iv()), aesencrypt(password, gen_key(), gen_iv())])
