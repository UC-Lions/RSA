#!/usr/bin/python3

#Generate custom RSA public/private key pair

from Crypto.PublicKey import RSA

# t is the tuple (n, e, d, p, q)
t = 1249110767794010895540410194153, 65537, 205119704640110252892051812353, 56244518227433, 22208577958531841
key = RSA.construct(t)
pv_key_string = key.exportKey()
with open ("private.pem", "w") as prv_file:
	print("{}".format(pv_key_string.decode()), file=prv_file)

pb_key_string = key.publickey().exportKey()
with open ("public.pem", "w") as pub_file:
	print("{}".format(pb_key_string.decode()), file=pub_file)