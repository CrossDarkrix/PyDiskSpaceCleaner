#coding:utf-8

import os

print("Deleting TMP Files.....")

try:
	os.remove('JunkFile0.tmp')
	os.remove('JunkFile2.tmp')
	os.remove('JunkFile3.tmp')
except OSError:
	pass
	
print("Deleting Complete!") 
