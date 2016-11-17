# -*- coding: utf-8 -*-
"""
Task0001: generate m number of unique activation codes of length n 
"""
from string import ascii_letters
from itertools import chain
import numpy as np

def generateACode():
    codeList=np.random.choice(pool,length).tolist()
    return ''.join(codeList)

def addCode():
    codes=set() # ensure all codes are unique.
    while len(codes)<number:
        ACode=generateACode()
        codes.add(ACode)
    return codes

if __name__=='__main__':
    pool=list(chain(range(0,10),ascii_letters))   #create a pool of characters to choose form
    length=int(input('Enter the length of the activtation code: '))
    number=int(input('Enter the total number of activation code to be generated: '))
    codes=addCode()
    print (codes)