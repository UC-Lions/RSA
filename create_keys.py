#!/usr/bin/python3

#Generate RSA public/private key pair

from Crypto.PublicKey import RSA

#FIPS standards specify 1024, 2048, 3072
#FIPS recommends 2048
key = RSA.generate(2048)
pv_key_string = key.exportKey()
with open ("private.pem", "w") as prv_file:
	print("{}".format(pv_key_string.decode()), file=prv_file)

pb_key_string = key.publickey().exportKey()
with open ("public.pem", "w") as pub_file:
	print("{}".format(pb_key_string.decode()), file=pub_file)