import os
import hashlib

#function opens file being passed through the path and returns the MD5 digest
def getMD5(path):
	file = open(path)
	hash = hashlib.md5()
	hash.update(file.read().encode('utf-8'))
	return hash.hexdigest()
