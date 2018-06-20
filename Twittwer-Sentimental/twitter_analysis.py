#!/usr/bin/python3

#imports

import string
import tweepy
from textblob import TextBlob 
from nltk.corpus import stopwords 
import matplotlib.pyplot as plt

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

#Finding Data
get_data=connect.search(input("Enter the keyword:  "),count=100)
#print(type(get_data))

new_data=[]

#tweets are:

for i in get_data:
	temp=[j for j in i.text if j not in string.punctuation]
	new_data.append(''.join(temp))
	
x=0
good_data=[]

for i in new_data:
	temp=[i for i in new_data[x].split() if i not in stopwords.words('english')]
	good_data.append(' '.join(temp))
	x+=1
	print(good_data[-1])

# Check the polarity of tweets

negative,positive,neutral=0,0,0

for i in good_data:
	y=TextBlob(i)
	
	if y.sentiment[0]==0.0 :
		neutral+=1
	elif y.sentiment[0]>0.0  :
		positive+=1
	elif y.sentiment[0]<0.0 :
		negative+=1

a=['neutral','negative','positive']

b=[neutral,negative,positive]

plt.xlabel('Number of tweets')
plt.ylabel('Polarity in %')

plt.bar(a[0],b[0],label='neutral')
plt.bar(a[1],b[1],label='negative')
plt.bar(a[2],b[2],label='positive')

plt.grid()

plt.legend()
plt.show()
