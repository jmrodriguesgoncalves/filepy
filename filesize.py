import sys
import os
import hashlib


def getFilesize(path):
    filesize = os.path.getsize(path)
    return filesize