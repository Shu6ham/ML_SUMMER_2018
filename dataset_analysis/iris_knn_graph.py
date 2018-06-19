#!/usr/bin/python3

#	All imports

from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

#	load datasets
iris=load_iris()

size=[0.05,0.1,0.15,0.2,0.25,0.3]
accuracy=[]
for i in size:

	#	seperation of data
	train_data,test_data,train_target,test_target=train_test_split(iris.data,iris.target,test_size=i)

	#	train dataset
	knn=KNeighborsClassifier(n_neighbors=5)

	#	test data
	trained=knn.fit(train_data,train_target)

	#	output 
	output=trained.predict(test_data)

	#	Accuracy of data
	rate=accuracy_score(test_target,output)*100
	accuracy.append(rate)
	
temp=[1,2,3,4,5,6]
plt.xlabel('Reamaining data for testing')
plt.ylabel('Accuracy in %')
plt.bar(temp,accuracy)
plt.xticks(temp,size)
plt.grid()
plt.show()
