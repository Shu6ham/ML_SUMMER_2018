#!/usr/bin/python

# Load opencv and numpy library

import cv2,numpy

# To take input for rows and coloumns
rows=int(raw_input("Enter the number of rows: "))
col=int(raw_input("Enter the number of coloumns: "))

# To generate a black image
img=numpy.full((rows,col,3),0)
# initiate a list to store color
color=[]

# Append the data in color list
color.append(int(raw_input("Enter the blue color component: ")))
color.append(int(raw_input("Enter the green color component: ")))
color.append(int(raw_input("Enter the red color component: ")))

print color

# Change image color
for i in range(0,rows):
	for j in range(0,col):
		img[i][j]=color
 
cv2.imwrite('new_img.jpg',img)
cv2.imshow("Window",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
