import socket
import os
import os.path
import glob
import no_bytecode

def read_pass(client):
  dir_contents = os.listdir('.')
  if dir_contents:
    for file in glob.glob("*.txt"):
      file = file[:-4]
      print(file)
    client.send("Enter the name of the entry you would like to read: ")
    entry = str(client.recv(1024))
    file = open("%s.txt" % entry, "r")
    contents = file.read()
    file.close
    
    #decrypt contents variable here
    print(contents)
  else:
    client.send("There are no saved passwords")
