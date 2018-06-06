#!/usr/bin/python

#	Loading library opencv and numpy
import cv2
import numpy

#	Reading image in color mode
img=cv2.imread("/home/shubham/Downloads/flower.jpg")
size=img.shape
#	Print the shape of image
print size

cv2.imshow("Image1",img)
cv2.waitKey(0)	

print "ROI image is: "

img1=numpy.full((size[0]//2,size[1]//2,3),0)+img[0:size[0]//2,0:size[1]//2]

img[0:size[0]//2,0:size[1]//2] = img[size[0]//2:size[0],size[1]//2:size[1]]
img[size[0]//2:size[0],size[1]//2:size[1]] = img1


cv2.imwrite("ROI.jpg",img)
cv2.imshow("ROI Image",img)
cv2.waitKey(0)	
