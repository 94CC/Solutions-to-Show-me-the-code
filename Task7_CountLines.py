# -*- coding: utf-8 -*-
"""
有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。
A directory contains programs you have written.
Count the total number of lines of codes in each file, also list the counts for number of empty lines
and number of comment lines.
"""
import os
import re

class ProgramsCount:
    def __init__(self,file):
        self.file=file

    def readfile(self):
        totalNo=0
        emptylineNo=0
        commentlineNo=0
        while True:
            line=self.file.readline()
            #Remove white space at the beginning
            line=line.lstrip(' ')
            if line=='': #if we reach the end of the document or if the file is empty.
                break
            elif line=='\n':
                emptylineNo+=1
            elif re.search('^#',line) !=None: #if there exists a line that begins with #
                commentlineNo+=1
            totalNo+=1
        return totalNo,emptylineNo,commentlineNo
    

def main():
    indir=input("enter target directory: ")
    os.chdir(indir) 
    for infile in os.listdir(os.getcwd()):
        root,extension=os.path.splitext(infile)
        if extension=='.py':
            with open(infile) as f:
                print ("for file ", root)
                program=ProgramsCount(f)
                totalNo,emptylineNo,commentlineNo=program.readfile()
                print ("total number of lines: ",totalNo)
                print ("number of empty lines: ",emptylineNo)
                print ("number of comment lines: ",commentlineNo)
                
if __name__=='__main__':
    main()