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

        L = len(words)
        for i in range(L-1):
            first = words[i]
            second = words[i+1]
            # to remove symbols and special characters
            first = removeChars(first)
            second = removeChars(second)
            # to stem the data
            first = stemData(first)
            second = stemData(second)

            if first in stop_words or second in stop_words or first.strip() == "" or second.strip() == "" :
                pass 
            else :
                CombinedWord = first + "," + second
                print ('%s%s%d' % (CombinedWord, separator, 1))
        
if __name__ == "__main__":
    main()
