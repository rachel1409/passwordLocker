import socket
import os
import sys
import os.path
import csv
from PLcrypto import *
from aes import *
import no_bytecode

def checkVerification(client, message):
  if not message:
    client.shutdown(socket.SHUT_RDWR)
    client.close()
    sys.exit(1)
  else:
    return message

def save_pass(client, key, clientkey, aeskey):
  client.send(PLencrypt("Enter a name for this entry:", key, aeskey))
  entry = checkVerification(client, PLdecrypt(client.recv(1024), clientkey, aeskey))
  if not os.path.isfile("%s.csv" % entry):
    client.send(PLencrypt("Enter a username:", key, aeskey))
    username = checkVerification(client, PLdecrypt(client.recv(1024), clientkey, aeskey))
    client.send(PLencrypt("Enter a password:", key, aeskey))
    password = checkVerification(client, PLdecrypt(client.recv(1024), clientkey, aeskey))
    
    with open("%s.csv" % entry,"w+") as f:
       writer = csv.writer(f)
      writer.writerow([aesencrypt(username, enckey("../"), gen_iv()), aesencrypt(password, enckey("../"), gen_iv())])
  else:
    clearscrn()
    return "An entry with this name already exists.\n"    

  
