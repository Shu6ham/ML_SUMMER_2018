#!/usr/bin/python3

import numpy
from sklearn.datasets import load_iris
from statistics import mean
import matplotlib.pyplot as plt

iris=load_iris()

x=iris.data.reshape(1,600)[0,0:300]
print(x.shape)
y=iris.data.reshape(1,600)[0,300:600]
print(y.shape)

def slope():
	m=((mean(x)*mean(y))-(mean(x*y)))/((mean(x)**2)-mean(x**2))
	return m

def intercept():
	c=mean(y)-(mean(x)*slope())
	return c

print('slope= '+str(slope()))
print('intercept= '+str(intercept()))

plt.xlabel('Data')
plt.ylabel('Output')
plt.scatter(x,y)
Output=[(slope()*i+intercept()) for i in x]
plt.plot(x,Output,color='red')
plt.show()