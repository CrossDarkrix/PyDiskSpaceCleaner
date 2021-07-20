#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from random import random as rnd
from os.path import getsize as gs
from os import remove
import sys
from threading import Thread
from time import sleep

D = [str(rnd()) for AA in range(5)]
rData = (D[0]+D[1]+D[2]+D[3]+D[4]).replace('.','')
zData = (b'\x00\x00\x00\x00\x00\x00\x00\x00\x00').decode('utf-8')
rzData = rData + zData
DataPlus = (b'\x00').decode('utf-8')
Stopping_Cycle = ['0']

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
        Stopping_Cycle[0] = '1'
        JunkFile1 = round(gs('JunkFile0.tmp') / 1073741824)
        JunkFile2 = round(gs('JunkFile2.tmp') / 1073741824)
        JunkFile3 = round(gs('JunkFile3.tmp') / 1073741824)
        TotalSize = round(JunkFile1 + JunkFile2 + JunkFile3)
        print("|      Cleannig Complete        |\n|-------------------------------|")
        print("|                               |")
        print("|>>Filled Files:                |")
        print("|   JunkFile0.tmp: {JUNKFILE1}GB          |".format(JUNKFILE1=JunkFile1))
        print("|   JunkFile2.tmp: {JUNKFILE2}GB          |".format(JUNKFILE2=JunkFile2))
        print("|   JunkFile3.tmp: {JUNKFILE3}GB          |".format(JUNKFILE3=JunkFile3))
        print("|   TotalSize: {TOTALFILE}GB              |".format(TOTALFILE=TotalSize))
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

def Cycle_Animeation():
    print("|      Writing.....|            |", end="\r", flush=True)
    sleep(0.1)
    print("|      Writing...../            |", end="\r", flush=True)
    sleep(0.1)
    print("|      Writing.....-            |", end="\r", flush=True)
    sleep(0.1)
    print("|      Writing.....\\            |", end="\r", flush=True)
    sleep(0.1)

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

class Cycles(Thread):
    def __init__(self):
        Thread.__init__(self)
    def run(self):
        while True:
            Cycle_Animeation()
            if Stopping_Cycle[0] == '1':
                print("                                               ", end="\r", flush=True)
                break

def main():
    print("|-------------------------------|\n|   JunkFiles Create Cleanner   |\n|-------------------------------|")
    print("|  1: Random Fill Mode          |\n|  2: Zero Fill Mode            |\n|  3: Zero & Random Fill Mode   |\n|-------------------------------|")
    SelectMode = input(" SelectMode: ")
    print("|-------------------------------|\n|      Please Wait......        |\n|-------------------------------|")
    if SelectMode == '1':
        RandomFill().start()
        Cycles().start()
    elif SelectMode == '2':
        ZeroFill().start()
        Cycles().start()
    elif SelectMode == '3':
        ZeroandRandomFill().start()
        Cycles().start()
    else:
        sys.exit(0)

if __name__== '__main__':
    main()
