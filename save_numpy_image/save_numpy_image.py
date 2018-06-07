#!/usr/bin/python

#	Loading of opencv and numpy library

import cv2,numpy

#	Reading of images

img1 = cv2.imread('/home/shubham/Downloads/river.jpg')
img2 = cv2.imread('/home/shubham/Downloads/snow.jpg')
img3 = cv2.imread('/home/shubham/Downloads/nature2.jpg')

#	COnverting and Saving of images in numpy format

numpy.save('river.npy',img1)
numpy.save('snow.npy',img2)
numpy.save('nature2.npy',img3)