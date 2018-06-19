#!/usr/bin/python3

#	All Imports
from sklearn.datasets import load_iris
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

#	Loading of iris dataset
iris = load_iris()

#	Different sizes for test
size=[0.05,0.1,0.15,0.2,0.25,0.3]
accuracy=[]
for i in size:
#	Seperation of dataset 
	x,y,z,a=train_test_split(iris.data,iris.target,test_size=i)
#	train data set
	clf=tree.DecisionTreeClassifier()
	trained=clf.fit(x,z)
	output=trained.predict(y)
	rate=accuracy_score(a,output)*100
	accuracy.append(rate)
	
temp=[1,2,3,4,5,6]
plt.xlabel('Reamaining data for testing')
plt.ylabel('Accuracy in %')
plt.bar(temp,accuracy)
plt.xticks(temp,size)
plt.grid()
plt.show()
