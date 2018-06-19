#!/usr/bin/python3

#	All Imports
from sklearn.datasets import load_iris
from sklearn import tree
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

#	Loading of iris dataset
iris = load_iris()

#	Different sizes for test
size=[0.05,0.1,0.15,0.2,0.25,0.3]

dtc_accuracy=[]
for i in size:
#	Seperation of dataset 
	x,y,z,a=train_test_split(iris.data,iris.target,test_size=i)
#	train data set
	clf=tree.DecisionTreeClassifier()
	trained=clf.fit(x,z)
	output=trained.predict(y)
	rate=accuracy_score(a,output)*100
	dtc_accuracy.append(rate)
	

knn_accuracy=[]
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
	knn_accuracy.append(rate)

temp=[1.5,4.5,7.5,10.5,13.5,16.5]
temp1=[1,4,7,10,13,16]
temp2=[2,5,8,11,14,17]
plt.xlabel('Reamaining data for testing')
plt.ylabel('Accuracy in %')
plt.bar(temp1,dtc_accuracy,label='Decision Tree Classifier Accuracy')
plt.bar(temp2,knn_accuracy,label='KNN Accuracy')
plt.xticks(temp,size)
plt.legend()
plt.grid()
plt.show()
