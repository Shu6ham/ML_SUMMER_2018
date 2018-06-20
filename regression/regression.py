#!/usr/bin/python3

import numpy
from sklearn.datasets import load_iris
from statistics import mean
import matplotlib.pyplot as plt

iris=load_iris() 

x=numpy.array([1,2,3,4,5,6,7])
y=numpy.array([2,4,7,9,9,14,16])

def slope(x1,y1,x2,y2):
	m=(y2-y1)/(x2-x1)
	return m

total_slope=0
for i in range(0,len(x)-1):
	total_slope+=(slope(x[i],y[i],x[i+1],y[i+1]))

mean_slope=total_slope/(len(x)-1)

intercept=mean(y)-(mean(x)*mean_slope)

print('slope= '+str(mean_slope))
print('intercept= '+str(intercept))

plt.xlabel('Data')
plt.ylabel('Output')
plt.scatter(x,y)
Output=[(mean_slope*i+intercept) for i in x]
plt.plot(x,Output,color='red')
plt.show()

for i in x:	
	print(i*mean_slope+intercept)