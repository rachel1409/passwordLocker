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

def delete_pass(client, key, clientkey, aeskey):
  contents = ""
  dir_contents = os.listdir('.')
  if dir_contents:
    for file in glob.glob("*.csv"):
      file = file[:-4]
      print(file)
    client.send(PLencrypt("Enter the name of the entry you would like to delete: ", key, aeskey))
    entry = PLdecrypt(client.recv(1024), clientkey, aeskey)
    if not entry:
      client.shutdown(socket.SHUT_RDWR)
      client.close()
      sys.exit(1)
    
    if os.path.isfile("%s.csv" % entry):  
      os.remove("%s.csv" % entry)
      clearscrn()
      return "Entry deleted!\n"
    else:
      clearscrn()
      return "There is no entry with that name\n"
  else:
    clearscrn()
    return "There are no saved passwords\n"
