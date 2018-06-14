#!/usr/bin/python3

# imports
from nltk.tokenize import sent_tokenize,word_tokenize
from nltk.corpus import stopwords

f=open("hello.txt",'r')

# data reading from file
new_data=f.read().split()
print (new_data)

print("-"*20)

# Removing of stopwords
final_data=[i for i in new_data if i not in stopwords.words('english')]
print (final_data)
