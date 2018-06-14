#!/usr/bin/python3

#imports

import string
import tweepy
from textblob import TextBlob 
from nltk.corpus import stopwords 

#Creating consumer key and secret key

consumer_key='Td2YwYc2fae8Mam0HmsekIC4H'
consumer_secret='Um1SJ9wSEsvbySvtV1NVFArSPrWf2LNlwxWlGYckXIGLfMojrB'

# Creating access and secrtet key

access_key='931131488187310085-JdlHLpZQWBtHTWLR5LmqaFjqune8PHi'
access_secret_key='W3Mf6YortHQLqrFG656yygNzzH5SFEIkGRvSeD5haPDGb'

# connecting to twitter

auth =  tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token=(access_key,access_secret_key)

#ConnectApi
connect=tweepy.API(auth)

connect=tweepy.API(auth)
connect=tweepy.API(auth)
#Finding Data
get_data=connect.search(input("Enter the keyword:  "),count=10)
#print(type(get_data))

new_data=[]

#tweets are:

for i in get_data:
	temp=[j for j in i.text if j not in string.punctuation]
	new_data.append(''.join(temp))
	print (new_data[-1])

print('*'*50)

x=0

good_data=[]

for i in new_data:
	temp=[i for i in new_data[x].split() if i not in stopwords.words('english')]
	good_data.append(' '.join(temp))
	x+=1
	print(good_data[-1])