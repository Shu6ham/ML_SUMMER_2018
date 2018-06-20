#!/usr/bin/python

# import cv2 and numpy library

import cv2,numpy,os

#	Function to create differences
def create_diff(x,y,z):
	diff1=cv2.absdiff(x,y)
	diff2=cv2.absdiff(y,z)
	diff3=cv2.bitwise_and(diff1,diff2)
	return diff3

#	To turn on the camera
cap = cv2.VideoCapture(0)

#	take pictures

img1=cap.read()[1]
img2=cap.read()[1]
img3=cap.read()[1]

#	Conversion of images into grayscale mode

gray1=cv2.cvtColor(cap.read()[1],cv2.COLOR_BGR2GRAY)
gray2=cv2.cvtColor(cap.read()[1],cv2.COLOR_BGR2GRAY)
gray3=cv2.cvtColor(cap.read()[1],cv2.COLOR_BGR2GRAY)

while (1):

	new_img=create_diff(gray1,gray2,gray3)
	cv2.imshow("Motion",new_img)

	temp_img=cap.read()[1]
	cv2.imshow("Original",temp_img)

	#	Shifting of images to contionuos detecting
	gray1=gray2
	gray2=gray3
	gray3=cv2.cvtColor(temp_img,cv2.COLOR_BGR2GRAY)

	if cv2.waitKey(1) & 0xFF==ord('q') :
		break

cv2.destroyAllWindows()
cap.release()
