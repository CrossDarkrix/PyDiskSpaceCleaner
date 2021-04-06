# coding:utf-8

import random
from os.path import getsize
from os import remove

Data = str(random.random()+random.random()+random.random()+random.random()+random.random()+random.random()+random.random()+random.random()+random.random()+random.random()+random.random()+random.random()+random.random()+random.random()+random.random()+random.random()+random.random()+random.random()+random.random()+random.random()+random.random()+random.random()+random.random()+random.random()+random.random()+random.random())

Plus = (b'\x00').decode()

def main():
	print('█████████████████')
	print('█	Create JunkFiles Cleanner   █')
	print('█	Please Wait.........	    █')
	print('█████████████████')
	
	f = open('JunkFile0.tmp','a')
	g = open('JunkFile2.tmp','a')
	h = open('JunkFile3.tmp','a')
	try:
		while True:
			f.write(Data)
			f.write(Data)
			g.write(Data)
			g.write(Data)
			h.write(Data)
			h.write(Data)
		f.close()
		g.close()
		h.close()
	except OSError:
		writing_to_bytes()


def writing_to_bytes():
	f = open('JunkFile0.tmp','a')
	g = open('JunkFile2.tmp','a')
	h = open('JunkFile3.tmp','a')
	try:
		while True:
			f.write(Plus)
			g.write(Plus)
			h.write(Plus)
		f.close()
		g.close()
		h.close()
	except OSError:
		totalsize = ((getsize('JunkFile0.tmp') / 1073741824) + (getsize('JunkFile2.tmp') / 1073741824) + (getsize('JunkFile3.tmp') / 1073741824))
	print('███  Cleanning Complete! ███')
	print('█████████████████')
	print('\n')
	print('█Filled Files:')
	print(" 	JunkFile0.tmp:",round(int(getsize('JunkFile0.tmp') / 1073741824), 2),"GB 	 ")
	print(" 	JunkFile2.tmp:",round(int(getsize('JunkFile2.tmp') / 1073741824), 2),"GB	 ")
	print(" 	JunkFile3.tmp:",round(int(getsize('JunkFile3.tmp') / 1073741824), 2),"GB	 ")
	print(" 	 Total Writed:",round(int(totalsize), 2),"GB	 ")
	print('\n')
	print('█████████████████')
	remove('JunkFile0.tmp')
	remove('JunkFile2.tmp')
	remove('JunkFile3.tmp')

if __name__ == '__main__':
	main()

