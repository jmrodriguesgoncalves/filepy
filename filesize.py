import sys
import os
import hashlib

#function returns size of file only
def getFilesize(path):
    filesize = os.path.getsize(path)
    return filesize