#!/usr/bin/python3

from Crypto.PublicKey import RSA

f = open('private.pem','r')
key = RSA.importKey(f.read())
print(key.d)
print(key.e)