"""
Exercise 6:
You have a diretory in which your diaries are stored in the form of txt files. 
Find the ten most important words in each diary.
"""
import os
import re

class ImptWords():
    def __init__(self,file):
        self.file=open(file)
        self.words=re.findall('[a-zA-Z]+',self.file.read().lower()) #ensure we are not counting e.g Family and family differently.
        self.file.close()
        
    def GetImptWords(self):
        filtered_words=self.filter_words() #get rid of unimportant words& characters
        words_dict=self.count_WordFrequency(filtered_words) #a dictionary storing words and their frequency
        TopWords=self.select_TopWords(words_dict)
        return TopWords
    
    def filter_words(self):
        """get words from the txt file. Exclude white space, punctuations, and line break characters."""
        redundantWords=['a','an','the','for','of','is','are','or','by','to','we','on','with','we','you','it','in','and','from','they','as','his','her','he']
        words=[i for i in self.words if i not in redundantWords]
        return words

    def count_WordFrequency(self,filtered_words):
        word_no={}
        for i in filtered_words:
            word_no[i]=word_no.get(i,0)+1
        return word_no
    
    def select_TopWords(self,words_dict):
        sortedWord=sorted(words_dict,key=words_dict.__getitem__,reverse=True)[0:10] #get the top ten words
        topword_dict={}
        for i in sortedWord:
            topword_dict[i]=words_dict[i]
        return topword_dict
    
def process_file(file):
    myModel=ImptWords(file)
    myImptWords=myModel.GetImptWords()
    return myImptWords
    
def main():
    indir=input("Enter filepath: ")
    os.chdir(indir)
    for infile in os.listdir(os.getcwd()):
        extension=os.path.splitext(infile)[1]
        if extension=='.txt':
            ImptWords=process_file(infile)
            print ("Important words for %s are: "%infile)
            print (ImptWords)
            
if __name__=='__main__':
    main()
