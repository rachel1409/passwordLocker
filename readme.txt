To run the program, type in terminal "python Program.py". all other files run in the background.

client.py will be the user interaction with the program.

server.py will be the server logic of handling client data such as passwords and accounts.

CreateAccount.py will handle creating user accounts and storing them in a text file.

Login.py will read from text file to verify user account and password.

PasswordHandler.py will check passwords to see if they meet the requirements.

Don't worry about file "no_bytecode".

12/1/17 3PM
The password saving feature has been implemented.
Users can now save passwords to their account and read their own passwords.

The program's login feature has been fledged out.
Users can't login to another account if they are already logged in.
Additionally users cannot save or read passwords unless they are logged in.

Crypto functions still need to be implemented.

There is also a bug where once an unsuccessful login has been beformed a successful login cannot occur.
