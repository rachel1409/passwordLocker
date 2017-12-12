import socket
import os
import sys
import os.path
import csv
from PLcrypto import *
from aes import *
from ClearScreen import *
import no_bytecode

# check if signature is verified
def checkVerification(client, message):
  if not message: #shutdown connection
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
    
    # write encrypted username and password to new entry's file
    with open("%s.csv" % entry,"w+") as f:
      writer = csv.writer(f)
      writer.writerow([aesencrypt(username, enckey("../"), gen_iv()), aesencrypt(password, enckey("../"), gen_iv())])
    clearscrn()
    return "Password saved!\n"
  else:
    clearscrn()
    return "An entry with this name already exists.\n"    

  
