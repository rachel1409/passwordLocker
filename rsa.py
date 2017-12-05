from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto import Random

def gen_privkey():
	random_generator = Random.new().read
	rsakey = RSA.generate(1024, random_generator)
	return rsakey

def gen_pubkey(rsakey):
	pubkey = rsakey.publickey()
	return pubkey

def rsaencrypt(message, key):
	cipher = PKCS1_OAEP.new(key)
	ciphertext = cipher.encrypt(message)
	return ciphertext

def rsadecrypt(ciphertext, key):
	cipher = PKCS1_OAEP.new(key)
	plaintext = cipher.decrypt(ciphertext)
	return plaintext

def get_pubkey(file_name):
	with open(file_name, 'r') as f:
		key = RSA.importKey(f.read())
	return key

def save_pubkey(file_name, key):
	with open(file_name, 'w+') as f:
		f.write(key.exportKey('PEM'))