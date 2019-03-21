#!/usr/bin/python3

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64
import sys

def decrypt_data(blob, key):
	rsa_key = RSA.importKey(key)
	rsa_key = PKCS1_OAEP.new(rsa_key)
	blob = base64.b64decode(blob)
	decrypted = rsa_key.decrypt(blob)
	return decrypted

def encrypt_data(blob, key):
	rsa_key = RSA.importKey(key)
	rsa_key = PKCS1_OAEP.new(rsa_key)
	encrypted = rsa_key.encrypt(blob)
	return base64.b64encode(encrypted)

def printUsage():
	print("\nUsage:\n\trsa.py [option] [pem-file] [input-filename] [output-filename]")
	print("\n[option]:\n\te\tencrypt\n\td\tdecrypt")
	print("\n[pem-file]:\n\tPEM file containing RSA key\n\tIf option==e, use public key PEM file\n\tIf option==d, use private key PEM file")
	print("\n[input-filename]:\n\tThe name of the input file\n\tIf option==e, this is a plaintext file\n\tIf option==d, this is a ciphertext file")
	print("\n[output-filename]:\n\tThe name of the output file\n\tIf option==e, this is a ciphertext file\n\tIf option==d, this is a plaintext file")
	
def main(argv):
	if (len(sys.argv) != 5):
		printUsage()
		sys.exit()
	
	#parse command line arguments:
	option, keyfile, inputfile, outputfile = argv
	
	#Read the pem file (key):
	fd = open(keyfile, "rb")
	key = fd.read()
	fd.close()
	
	#Read the input file:
	fd = open(inputfile, "rb")
	blob = fd.read()
	fd.close()

	if (option == 'e'):
		new_blob = encrypt_data(blob, key)
	elif (option == 'd'):
		new_blob = decrypt_data(blob, key)
	else:
		print("Invalid Option")
		printUsage()
		sys.exit()

	#Write the encrypted or decrypted contents to a file
	fd = open(outputfile, "wb")
	fd.write(new_blob)
	fd.close()
	print("\nComplete\n")

	
if __name__ == "__main__":
   main(sys.argv[1:])