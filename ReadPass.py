import socket
import os
import sys
import csv
import os.path
import glob
from PLcrypto import *
from aes import *
import no_bytecode
from ClearScreen import *

def read_pass(client, key, clientkey, aeskey):
  contents = ""
  dir_contents = os.listdir('.')
  if dir_contents:
    for file in glob.glob("*.csv"):
      file = file[:-4]
      print(file)
    client.send(PLencrypt("Enter the name of the entry you would like to read: ", key, aeskey))
    entry = PLdecrypt(client.recv(1024), clientkey, aeskey)
    if not entry: # verification failed - shutdown connection
      client.shutdown(socket.SHUT_RDWR)
      client.close()
      sys.exit(1)
    
    if os.path.isfile("%s.csv" % entry): 
      # decrypt username and password and save both in variable
      with open("%s.csv" % entry, "r") as f:
        reader = csv.reader(f)
        for row in reader:
          contents = "username: "+aesdecrypt(row[0], enckey('../'))+"\npassword: "+aesdecrypt(row[1], enckey('../'))+"\n"

      return contents
    else:
      clearscrn()
      return "There is no entry with that name\n"
  else:
    clearscrn()
    return "There are no saved passwords\n"
