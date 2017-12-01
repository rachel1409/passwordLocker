import socket
import os
import os.path
import no_bytecode

def save_pass(client):
  client.send("Enter a name for this entry:")
  entry = str(client.recv(1024))
  client.send("Enter a username:")
  username = str(client.recv(1024))
  client.send("Enter a password:")
  password = str(client.recv(1024))

  #Convert username and password to encrypted data here and replace variables below with encrypted variables        
        
  file = open("%s.txt" % entry,"w+")		
  file.write(username + ", " + password + "\n")
  file.close()
