#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from random import random as rnd
from os.path import getsize as gs
from os import remove
import sys
from threading import Thread

# Data
D = [str(rnd()) for AA in range(5)]
rData = (D[0]+D[1]+D[2]+D[3]+D[4]).replace('.','')
zData = (b'\x00\x00\x00\x00\x00\x00\x00\x00\x00').decode('utf-8')
rzData = rData + zData
DataPlus = (b'\x00').decode('utf-8')

def writing_byte():
    add_f = open('JunkFile0.tmp','a')
    add_g = open('JunkFile2.tmp','a')
    add_h = open('JunkFile3.tmp','a')

    try:
        while True:
            add_f.write(DataPlus)
            add_g.write(DataPlus)
            add_h.write(DataPlus)
        add_f.close()
        add_g.close()
        add_h.close()
    except OSError:
        JunkFile1 = round(gs('JunkFile0.tmp') / 1073741824)
        JunkFile2 = round(gs('JunkFile2.tmp') / 1073741824)
        JunkFile3 = round(gs('JunkFile3.tmp') / 1073741824)
        print("|      Cleannig Complete        |\n|-------------------------------|")
        print("|                               |")
        print("|>>Filled Files:                |")
        print("|\tJunkFile0.tmp: {JUNKFILE1}GB\t\t\t|".format(JUNKFILE1=JunkFile1))
        print("|\tJunkFile2.tmp: {JUNKFILE2}GB\t\t\t|".format(JUNKFILE2=JunkFile2))
        print("|\tJunkFile3.tmp: {JUNKFILE3}GB\t\t\t|".format(JUNKFILE3=JunkFile3))
        print("|                               |")
        print("|-------------------------------|")
        remove('JunkFile0.tmp')
        remove('JunkFile2.tmp')
        remove('JunkFile3.tmp')

def mode_RandomFill():
    write_file_f = open('JunkFile0.tmp','a')
    write_file_g = open('JunkFile2.tmp','a')
    write_file_h = open('JunkFile3.tmp','a')
    try:
        while True:
            write_file_f.write(rData)
            write_file_g.write(rData)
            write_file_h.write(rData)
        write_file_f.close()
        write_file_g.close()
        write_file_h.close()
    except OSError:
        writing_byte()
    except KeyboardInterrupt:
        remove('JunkFile0.tmp')
        remove('JunkFile2.tmp')
        remove('JunkFile3.tmp')

def mode_ZeroFill():
    write_file_f = open('JunkFile0.tmp','a')
    write_file_g = open('JunkFile2.tmp','a')
    write_file_h = open('JunkFile3.tmp','a')
    try:
        while True:
            write_file_f.write(zData)
            write_file_g.write(zData)
            write_file_h.write(zData)
        write_file_f.close()
        write_file_g.close()
        write_file_h.close()
    except OSError:
        writing_byte()
    except KeyboardInterrupt:
        remove('JunkFile0.tmp')
        remove('JunkFile2.tmp')
        remove('JunkFile3.tmp')

def mode_Zero_and_Rnadom():
    write_file_f = open('JunkFile0.tmp','a')
    write_file_g = open('JunkFile2.tmp','a')
    write_file_h = open('JunkFile3.tmp','a')
    try:
        while True:
            write_file_f.write(rzData)
            write_file_g.write(rzData)
            write_file_h.write(rzData)
        write_file_f.close()
        write_file_g.close()
        write_file_h.close()
    except OSError:
        writing_byte()
    except KeyboardInterrupt:
        remove('JunkFile0.tmp')
        remove('JunkFile2.tmp')
        remove('JunkFile3.tmp')

class RandomFill(Thread):
    def __init__(self):
        Thread.__init__(self)
    def run(self):
        mode_RandomFill()

class ZeroFill(Thread):
    def __init__(self):
        Thread.__init__(self)
    def run(self):
        mode_ZeroFill()

class ZeroandRandomFill(Thread):
    def __init__(self):
        Thread.__init__(self)
    def run(self):
        mode_Zero_and_Rnadom()

def main():
    print("|-------------------------------|\n|   JunkFiles Create Cleanner   |\n|-------------------------------|")
    print("|  1: Random Fill Mode\t\t\t|\n|  2: Zero Fill Mode\t\t\t|\n|  3: Zero & Random Fill Mode   |\n|-------------------------------|")
    SelectMode = input(" SelectMode: ")
    print("|-------------------------------|\n|      Please Wait......        |\n|-------------------------------|")
    if SelectMode == '1':
        RandomFill().start()
    elif SelectMode == '2':
        ZeroFill().start()
    elif SelectMode == '3':
        ZeroandRandomFill().start()
    else:
        sys.exit(0)

if __name__== '__main__':
    main()
