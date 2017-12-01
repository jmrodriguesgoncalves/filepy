import filename
import filesize
import md5
import sha1
path = 'data/mydata.txt'

def test_size():
    assert filesize.getFilesize(path) == 43

def test_name():
    assert filename.getFilename(path) == "mydata.txt"

def test_md5():
    assert md5.getMD5(path) == "9e107d9d372bb6826bd81d3542a419d6"
	
def test_sha1():
    assert sha1.getSHA1(path) =="2fd4e1c67a2d28fced849ee1bb76e7391b93eb12"




