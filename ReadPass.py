import socket
import os
import os.path
import glob
import no_bytecode

def read_pass(client):
  
  for file in glob.glob("*.txt"):
    dir_contents = os.listdir('.')
    if dir_contents:
      #file = file[:-4]
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
