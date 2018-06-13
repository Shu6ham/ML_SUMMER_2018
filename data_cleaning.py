#!/usr/bin/python3

# imports
import urllib.request
from bs4 import BeautifulSoup
from nltk.tokenize import sent_tokenize,word_tokenize
from nltk.corpus import stopwords

website='http://php.net'

# data downloading & reading

web_data=urllib.request.urlopen(website)
clean_data=web_data.read()

get_clean=BeautifulSoup(clean_data,'html5lib')

good_data=get_clean.get_text()

final_data=good_data.strip()

# Tokenization Process

'''new_data=[]

for i in good_data:
	new_data.append(i.split())

print (new_data) '''

new_data=word_tokenize(final_data)

for i in new_data:
	if i in stopwords.words('english'):
		new_data.remove(i)

print (new_data)