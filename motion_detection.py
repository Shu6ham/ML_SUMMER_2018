#!//usr/bin/python

import cv2,numpy

cap=cv2.VideoCapture(0)

while cap.isOpened():
	
	status,frame=cap.read()
	# inRange() function to detect only green color
	only_green=cv2.inRange(frame,(0,0,40),(10,10,255))
	cv2.imshow("detect",only_green)
	if cv2.waitKey(1) & 0xFF==ord('q'):
		break

cv2.destroyAllWindows()
cap.release()
