import socket
import os
import os.path
import glob
from rsa import *
from aes import *
import no_bytecode

def read_pass(client, key, clientkey):
  contents = ""
  dir_contents = os.listdir('.')
  if dir_contents:
    for file in glob.glob("*.txt"):
      file = file[:-4]
      print(file)
    client.send(rsaencrypt("Enter the name of the entry you would like to read: ", clientkey))
    entry = rsadecrypt(client.recv(1024), key)

    with open("%s.csv" % entry, "r") as f:
      reader = csv.reader()
      for row in reader:
        for r in row:
          contents = contents + aesdecrypt(r, key_gen()) + "\n"

    client.send(rsaencrypt(contents, clientkey))
  else:
    client.send(rsaencrypt("There are no saved passwords", clientkey))
