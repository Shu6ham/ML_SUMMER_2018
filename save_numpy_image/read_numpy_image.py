#!/usr/bin/python

#	Loading of opencv and numpy library

import cv2,numpy

#	Reading of numpy format images

img1=numpy.load('river.npy')
img2=numpy.load('snow.npy')
img3=numpy.load('nature2.npy')

#	Displaying the images

cv2.imshow("river",img1)
cv2.waitKey(0)
cv2.imshow("snow",img2)
cv2.waitKey(0)
cv2.imshow("nature2",img3)
cv2.waitKey(0)

cv2.destroyAllWindows()