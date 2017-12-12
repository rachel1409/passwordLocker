# Author: Anne Marie Bogar
# Last Updated: December 8, 2017
# aes.py implements AES-256 CBC mode encryption/decryption, padding, and generation of key and IV

from Crypto.Cipher import AES
from Crypto import Random
import base64

# generates AES key
def gen_key():
	key = Random.new().read(32)
	return base64.b64encode(key)
	#return key

# retrieves AES key from file
def get_key(filename):
	with open(filename, 'r') as f:
		key = f.read()
	#return base64.b64encode(key)
	return key

# generates IV
def gen_iv():
	iv = Random.new().read(AES.block_size)
	return iv

# encrypts message in AES-256 mode CBC
def aesencrypt(message, key, iv):
	cipher = AES.new(key, AES.MODE_CBC, iv)
	message = pad(message) #pad message before encrypting
	return base64.b64encode(iv + cipher.encrypt(message))

# decrypts message with AES-256 mode CBC
def aesdecrypt(ciphertext, key):
	ciphertext = base64.b64decode(ciphertext) # decode ciphertext
	iv = ciphertext[:AES.block_size] # retrieve IV from ciphertext
	cipher = AES.new(key, AES.MODE_CBC, iv)
	return unpad(cipher.decrypt(ciphertext[AES.block_size:])).decode('utf-8')

# pad message before encryption
def pad(message):
	return message + (AES.block_size - len(message) % AES.block_size) * chr(AES.block_size - len(message) % AES.block_size)

# unpad message after decryption
def unpad(message):
	return message[:-ord(message[len(message)-1:])]
