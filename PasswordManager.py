import socket
import os
import os.path
import no_bytecode
from SavePass import *
from ReadPass import *

def manage_pass(client):
  tempbool = True
  while tempbool == True:
    client.send("Press 1 to save a username and password\nPress 2 to read a username and password\nPress 3 to go back to the main menu")
    response = client.recv(1024)
    
    if response == '1':
      save_pass(client)
      
    elif response == '2':
    read_pass(client)
    
  elif response == '3':
    tempbool = False
    
