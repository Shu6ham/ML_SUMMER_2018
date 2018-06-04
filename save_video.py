#!/usr/bin/python

import cv2

cap=cv2.VideoCapture(0)

# To get the height and width of frame
width=cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height=cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

# To get supported video format       XVID for .avi format
video_format=cv2.VideoWriter_fourcc(*'XVID')

# To get output of video for saving                     F.P.S  < Height and Width of Frame >
video_output=cv2.VideoWriter('Shubham.avi',video_format,30.0,(int(width),int(height)))
	 
while cap.isOpened():
	status,frame=cap.read()
	cv2.imshow("window",frame)
	# To store the video's output
	video_output.write(frame)
	
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cv2.destroyAllWindows()	
cap.release()

