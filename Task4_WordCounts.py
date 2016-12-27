# -*- coding: utf-8 -*-
"""
Task 0004: generate counts of different word's occurrences.
"""

import sys
import re
import pandas as pd

def get_words():
    """get words from the txt file. Exclude white space, punctuations, and line break characters."""
    words=re.findall('[a-zA-Z]+',f.read().lower()) 
    #ensure we are not counting different forms(i.e upper/lower letter) of the same word separately
    return words

def count_words():
    word_no={}
    for i in words:
        word_no[i]=word_no.get(i,0)+1
    return word_no

if __name__=='__main__':
    txtfile=sys.argv[1]
    with open(txtfile) as f:
        words=get_words()
        word_no=count_words() #alternative: use collections.Counter method straightaway
        print (pd.Series(word_no))#organise data into a table.
