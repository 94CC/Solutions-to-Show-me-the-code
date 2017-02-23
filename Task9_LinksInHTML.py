# -*- coding: utf-8 -*-
"""
Find links in an html document
"""
import sys
import os
from bs4 import BeautifulSoup
import re

class Links:
    def __init__(self,file):
        self.htmlsoup=BeautifulSoup(file,"lxml")
    def findLinks(self):
        links=[]
        for tag in self.htmlsoup.find_all(href=re.compile('.+')):
            links.append(tag['href'])
        return links

def main():
    file=sys.argv[1]
    extension=os.path.splitext(file)[1]
    if extension=='.html':
        with open(file) as f:
            htmlModel=Links(f)
            links=htmlModel.findLinks()
            print (links)
    else:
        print ("wrong file format!")

if __name__=='__main__':
    main()