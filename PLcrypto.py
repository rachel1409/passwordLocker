# Author: Anne Marie Bogar
# Last Updated: December 8, 2017
# PLcrypto.py implements message authentication with RSA digital signature and AES-256 CBC mode encryption/decryption

from aes import *
from rsa import *
import socket
import base64

# digital signature and AES encryption
def PLencrypt(message, privkey, aeskey):
	aeskey = base64.b64decode(aeskey) # decode aes key
	signtext = sign(message, privkey) # sign message with RSA private key
	return aesencrypt(signtext, aeskey, gen_iv()) #encrypt message and signature with AES-256 mode CBC and new IV

# AES decryption and signature verification
def PLdecrypt(ciphertext, pubkey, aeskey):
	aeskey = base64.b64decode(aeskey) # decode aes key
	signtext = aesdecrypt(ciphertext, aeskey) # decrypt message with AES-256 mode CBC
	if not verify(signtext[172:], signtext[:172], pubkey): # check digital signature verification
		print "Verification Failed"
		return False
	else:
		return signtext[172:]

# retrieve AES key known only to the server
def enckey(prefix=""):
	return get_key(prefix+"aes.txt")
