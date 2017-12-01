import os
import hashlib

#function opens file being passed through the path and returns the SHA-1 digest
def getSHA1(path):
	file = open(path)
	hash = hashlib.sha1()
	hash.update(file.read().encode('utf-8'))
	return hash.hexdigest()