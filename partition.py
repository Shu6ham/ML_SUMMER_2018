#!/usr/bin/python

#	Loading library opencv and numpy
import cv2
import numpy

#	Reading image in color mode
img=cv2.imread("/home/shubham/Downloads/flower.jpg")
size=img.shape
#	Print the shape of image
print size

part=int(raw_input("Enter the part required: \n"))

#	Partition image 
img1=img[0:size[0]//part , 0:size[1]//part]
#	Display the image
cv2.imshow("Image1",img1)
cv2.waitKey(0)	

#	Rest part of image  
cv2.rectangle(img,(0,0),(size[1]//part,size[0]//part),(255,255,255),-1)
cv2.imshow("Image2",img)
cv2.waitKey(0)

