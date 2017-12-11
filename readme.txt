To run the program, type in terminal "python Program.py". all other files run in the background.

**This code will run best on a Linux machine

The files in this program consist of:
  Client/Server:
    - client.py handles the user interaction with the program.
    - server.py handles the server logic of handling client data such as passwords and accounts.
  Password Locker:
    - CreateAccount.py handles creating user accounts and storing them in a text file.
    - Login.py will read from text file to verify user account and password.
    - PasswordHandler.py will check passwords to see if they meet the requirements.
    - ClearScreen.py is just for keeping the console screen clear while navigating menus
    - PasswordManager.py manages the password menu
    - ReadPass.py reads saved user passwords
    - SavePass.py saves user passwords
    - DeletePass.py deletes user passwords
  Cryptography:
    - aes.py manages our encryption function file for AES
    - PLcrypto.py manages message authentication
    - rsa.py manages digital signatures

Don't worry about file "no_bytecode".

The program will generate several files: a folder for the user, several .pyc python files, and a client.pem and a server.pem
