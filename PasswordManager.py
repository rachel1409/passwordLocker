import socket
import os
import sys
import os.path
import no_bytecode
from SavePass import *
from PLcrypto import *
from ReadPass import *
from ClearScreen import *

def manage_pass(client, key, clientkey, aeskey):
  tempbool = True
  message = ""
  while tempbool == True:
    client.send(PLencrypt(message+"Press:\n- 1 to save username/password\n- 2 to read username/password\n- 3 for main menu", key, aeskey))
    response = PLdecrypt(client.recv(1024), clientkey, aeskey)
    if not response:
      client.shutdown(socket.SHUT_RDWR)
      client.close()
      sys.exit(1)
    
    if response == '1':
      clearscrn()
      save_pass(client, key, clientkey, aeskey)
      
    elif response == '2':
      clearscrn()
      message = read_pass(client, key, clientkey, aeskey)
    
    elif response == '3':
      tempbool = False
    
