import socket
import os
import os.path
import no_bytecode
from SavePass import *
from rsa import *
from ReadPass import *
from ClearScreen import *

def manage_pass(client, key, clientkey):
  tempbool = True
  while tempbool == True:
    client.send(rsaencrypt("Press:\n- 1 to save username/password\n- 2 to read username/password\n- 3 for main menu", clientkey))
    response = rsadecrypt(client.recv(1024), key)
    
    if response == '1':
      save_pass(client, key, clientkey)
      
    elif response == '2':
      #clearscrn()
      read_pass(client, key, clientkey)
    
    elif response == '3':
      tempbool = False
    
