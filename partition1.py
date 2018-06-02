#!/usr/bin/python

#	Loading library cv2 and numpy
import cv2
import numpy

#	Reading the image
img=cv2.imread("/home/shubham/Downloads/flower.jpg",cv2.IMREAD_COLOR)
size=img.shape
print size


part=int(raw_input("Enter the part required(1/2/3/4) from both coloumn and row: \n"))

print "Max possible image of that sizes: \n"
for i in range(0,part):
	for j in range(0,part):
		#  x and x1 for coloumn range
		x=j*(size[1]//part)
		x1=(j+1)*(size[1]//part)
		#  y and y1 for row range 	
		y=i*(size[0]//part)
		y1=(i+1)*(size[0]//part)
		#  New image			
		img1=img[y:y1,x:x1]
		cv2.imshow("img"+str(i)+str(j),img1)
		cv2.waitKey(0)

		
