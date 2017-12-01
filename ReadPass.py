import socket
import os
import os.path
import no_bytecode

def read_pass(client):
  file = open("%s.txt" % entry, "r")
  contents = file.read()
  file.close
  
  #decrypt contents variable here
  
  print(contents)
