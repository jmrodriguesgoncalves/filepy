import os
import hashlib


def getSHA1(path):
	file = open(path)
	hash = hashlib.sha1()
	hash.update(file.read().encode('utf-8'))
	return hash.hexdigest()