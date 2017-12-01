import os
import hashlib


def getMD5(path):
	file = open(path)
	hash = hashlib.md5()
	hash.update(file.read().encode('utf-8'))
	return hash.hexdigest()
