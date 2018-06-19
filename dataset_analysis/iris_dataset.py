#!/usr/bin/python3

#imports

import numpy 
from sklearn.datasets import load_iris
from sklearn import tree

# Collecting data

iris = load_iris()

#Trainig datasets
# Removing this position data for trained datasets
x=[0,50,100]

#print(iris.data[x])

target_training=numpy.delete(iris.target,x)

data_training=numpy.delete(iris.data,x,axis=0)

# Using Classifier to train data sets

cls=tree.DecisionTreeClassifier()
trained=cls.fit(data_training,target_training)

output=trained.predict([[5.1,3.5,1.4,1.4]])

if output==[0]:
	print("Setosa")
elif output==[1]:
	print("Versicolor")
elif output==[2]:
	print ("Veginica")
