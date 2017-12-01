import sys
import os
import hashlib

#function returns name of file only
def getFilename(path):
    filename = os.path.basename(path)
    return filename
