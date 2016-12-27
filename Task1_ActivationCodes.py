"""
Task0001: generate m number of unique activation codes of length n 
"""
from string import ascii_letters
from itertools import chain
import numpy as np

class Activ_code:
    def __init__(self,length,number):
        """length: length of each code
        number: number of codes to be generated"""
        self.length=length
        self.number=number
        self.pool=list(chain(range(0,10),ascii_letters)) #create a pool of characters to choose from
        
    def generateACode(self):
        codeList=np.random.choice(self.pool,self.length).tolist()
        return ''.join(codeList)

    def addCode(self):
        codes=set() # ensure all codes are unique.
        while len(codes)<self.number:
            ACode=self.generateACode()
            codes.add(ACode)
        return codes

def main():
    length=int(input('Enter the length of the activtation code(characters): '))
    number=int(input('Enter the total number of activation code to be generated: '))
    MyActiv_code=Activ_code(length,number)
    codes=MyActiv_code.addCode()
    print (codes)
    return codes
    
if __name__=='__main__':
    main()
