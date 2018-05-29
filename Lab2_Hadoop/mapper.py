#!/usr/bin/python
"""A more advanced Mapper, using Python iterators and generators."""
import re 
import sys
import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

def read_input(file):
    for line in file:
        # split the line into words
        yield line.split()

def removeChars(words):
    words = words.replace('“','')
    words = words.replace('’','')
    words = words.replace('”','')
    words = words.replace('.','')
    words = words.replace(',','')
    words = words.replace(':','') 
    words = words.replace(';','')
    words = words.replace('(','')
    words = words.replace(')','')
    words = words.replace('!','')
    words = words.replace('?','')
    words = words.replace('$','') 
    words = words.replace('@','')
    words = words.replace('#','')
    words = words.replace('&','')
    words = words.replace('^','')
    words = words.replace('[','')
    words = words.replace(']','')
    words = words.replace('{','')
    words = words.replace('}','')
    words = words.replace('%','')
    words = words.replace('*','')
    words = words.replace('\'','')
    words = words.replace('\"','')
    words = words.replace('+','')
    words = words.replace('-','')
    words = words.replace('http','')
    words = words.replace('https','')
    return words
        
def stemData(word):
    ps = PorterStemmer()
    word = ps.stem(word)
    return word

def main(separator='\t'):
    # input comes from STDIN (standard input)
    data = read_input(sys.stdin)
    stop_words = set(stopwords.words('english'))
    
    for words in data:
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        
        # tab-delimited; the trivial word count is 1

        
        for word in words:
            # to remove symbols and special characters
            word = removeChars(word)
            # to stem the data
            word = stemData(word)
        
            if word in stop_words:
                pass 
            else :
                print ('%s%s%d' % (word, separator, 1))

if __name__ == "__main__":
    main()
