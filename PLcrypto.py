from aes import *
from rsa import *
import socket
import base64

def PLencrypt(message, privkey, aeskey):
	aeskey = base64.b64decode(aeskey)
	signtext = sign(message, privkey)
	return aesencrypt(signtext, aeskey, gen_iv())

def PLdecrypt(ciphertext, pubkey, aeskey):
	aeskey = base64.b64decode(aeskey)
	signtext = aesdecrypt(ciphertext, aeskey)
	if not verify(signtext[172:], signtext[:172], pubkey):
		print "Verification Failed"
		return False
	else:
		return signtext[172:]

def enckey(prefix=""):
	return get_key(prefix+"aes.txt")
