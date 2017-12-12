# Author: Anne Marie Bogar
# Last Updated: December 8, 2017
# rsa.py implements RSA encryption/decryption, digital signature, and creation of RSA key pair

from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256
import base64

# generate RSA private key
def gen_privkey():
	random_generator = Random.new().read
	rsakey = RSA.generate(1024, random_generator)
	return rsakey

# generate RSA public key using private key
def gen_pubkey(rsakey):
	pubkey = rsakey.publickey()
	return pubkey

# encrypt message with RSA public key
def rsaencrypt(message, key):
	cipher = PKCS1_OAEP.new(key)
	ciphertext = cipher.encrypt(message)
	return ciphertext

# decrypt ciphertext with RSA private key
def rsadecrypt(ciphertext, key):
	cipher = PKCS1_OAEP.new(key)
	plaintext = cipher.decrypt(ciphertext)
	return plaintext

# retrieve public key from pem file
def get_pubkey(file_name):
	with open(file_name, 'r') as f:
		key = RSA.importKey(f.read())
	return key

# save public key to pem file
def save_pubkey(file_name, key):
	with open(file_name, 'w+') as f:
		f.write(key.exportKey('PEM'))

# sign message with RSA private key
def sign(message, key):
	h = SHA256.new(message) #create hash of message
	signer = PKCS1_v1_5.new(key)
	signature = signer.sign(h) #sign hash with private key
	return base64.b64encode(signature)+message

# verify signature with RSA public key
def verify(message, signature, key):
	h = SHA256.new(message) #create hash of message
	signature = base64.b64decode(signature)
	verifier = PKCS1_v1_5.new(key)
	if verifier.verify(h, signature): #check verification of hash with public key
		return True
	else:
		return False
