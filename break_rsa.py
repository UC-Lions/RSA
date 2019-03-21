#!/usr/bin/python3
#
#Breaking (weak) RSA
#Adam Duby, aduby@uccs.edu
#UC Lions, UCCS

from Crypto.PublicKey import RSA
from sympy import mod_inverse
from sympy import factorint
import sys

def get_d(e, n):
	factors = factorint(n, multiple=True)
	p = factors[0];
	q = factors[1];
	print("p   = ", int(p))
	print("q   = ", int(q))
	phi = int((int(p)-1)*(int(q)-1))
	print("phi = ", int(phi))
	return mod_inverse(e, int(phi))

def read_from_pem(filename):
	fd = open(filename, 'r')
	key = RSA.importKey(fd.read())
	fd.close()
	return get_d(key.e, key.n)

def printUsage():
	print("\nUsage:\n\tbreak_rsa.py [public.pem]")
	print("\n\t\tOR")
	print("\n\tbreak_rsa.py [e] [n]\n")

def main(argv):
	if (len(sys.argv) == 2):
		d = read_from_pem(argv[0])
	elif (len(sys.argv) == 3):
		d = get_d(int(argv[0]), int(argv[1]))
	else:
		printUsage()
		sys.exit()
	print('d   = ', int(d))

if __name__ == "__main__":
	main(sys.argv[1:])
