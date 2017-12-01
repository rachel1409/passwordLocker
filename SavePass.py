import socket
import os
import os.path
import no_bytecode

def save_pass(client)
  client.send("Enter a username:")
          username = str(client.recv(1024))
          if username != "":
               while True:
                   client.send("Enter a password:")
                   password = str(client.recv(1024))
                      if pw_check(password):
                          client.send("Account created!\n\n")
                          break
                      else:
                          client.send("Please enter a valid password.\n")
                 break
             else:
                  client.send("Please enter a valid username.\n")
          else:
              client.send("Username taken, try again.\n")
  
      data_file.write(username + ", " + password + "\n")
      data_file.close()
