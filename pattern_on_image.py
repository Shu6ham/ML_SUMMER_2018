#!/usr/bin/python

import cv2
import numpy

#	Function converts color to (B,G,R) mode

def color_to_bgr(color):
	if(color == "red"):
		return ((0,0,255))
	elif(color == "green"):
		return ((0,255,0))
	elif(color == "blue"):
		return ((255,0,0))
	elif(color == "white"):
		return ((255,255,255))
	else:
		return ((0,0,0))

#	Reading the image
img=cv2.imread("/home/shubham/Downloads/flower.jpg")
size=img.shape
print size

x='''
1.	To Draw a line
2.	To Draw a circle
3. 	TO Draw a rectangle
4.	To draw a polygon
5.	To draw a ellipse
6. 	To write text on image
7.	To save final changes 	
8.	Exit \n'''

while (1):
	print x	
	choice=int(raw_input("Enter your choice: "))

	#	To Draw the line on image	
	if(choice==1):
		print "Enter the coordinates of 1st point:\n"
		x1,y1=int(raw_input("x:  ")),int(raw_input("y:  "))
		print "Enter the coordinates of 2nd point:\n"
		x2,y2=int(raw_input("x:  ")),int(raw_input("y:  "))
		color=raw_input("Enter color in red/blue/green/white: \n")
		temp_img=cv2.line(img,(x1,y1),(x2,y2),color_to_bgr(color),5)		
		cv2.imshow("line",temp_img)
		cv2.waitKey(0)
		cv2.destroyAllWindows()
	
#	To Draw the circle on image
	elif(choice==2):
		print "Enter the coordinates of the center:\n"
		x1,y1=int(raw_input("x:  ")),int(raw_input("y:  "))
		print "Enter the radius of the circle: \n"
		radius=int(raw_input())
		color=raw_input("Enter color in red/blue/green/white: \n")
		temp_img=cv2.circle(img,(x1,y1),radius,color_to_bgr(color),-1)
		cv2.imshow("Circle",temp_img)
		cv2.waitKey(0)
		cv2.destroyAllWindows()

	#	To Draw the rectangle on image
	elif(choice==3):
		print "Enter the coordinates of top left corner:\n "
		x1,y1=int(raw_input("x:  ")),int(raw_input("y:  "))
		print "Enter the coordinates of bottom right corner:\n "
		x2,y2=int(raw_input("x:  ")),int(raw_input("y:  "))
		color=raw_input("Enter color in red/blue/green/white: \n")
		temp_img=cv2.rectangle(img,(x1,y1),(x2,y2),color_to_bgr(color),5)
		cv2.imshow("Rectangle",temp_img)
		cv2.waitKey(0)
		cv2.destroyAllWindows()

	#	To Draw the polygon on image
	elif(choice==4):
		corner=int(raw_input("Enter the numbers of corners:\n"))
		data=[]		
		for i in range(1,corner+1):
			temp_data=[]			
			temp_data.append(int(raw_input("Enter "+str(i)+"th corner x-cordinate: ")))
			temp_data.append(int(raw_input("Enter "+str(i)+"th corner y-cordinate: ")))
			data.append(temp_data)
		data=numpy.array(data)
		color=raw_input("Enter color in red/blue/green/white: \n")
		temp_img=cv2.polylines(img,[data],True,color_to_bgr(color),-1)
		cv2.imshow("Polygon",temp_img)
		cv2.waitKey(0)
		cv2.destroyAllWindows()

	#	To Draw the ellipse on image
	elif(choice==5):
		print "Enter the coordinates of centre:\n"
		x1,y1=int(raw_input("x:  ")),int(raw_input("y:  "))
		print "Enter half lengths of major and minor axis:\n"
		a,b=int(raw_input("a:  ")),int(raw_input("b:  "))
		angle=int(raw_input("Enter the rotating angle of ellipse:\n"))
		start_angle=int(raw_input("Enter the starting angle of ellipse:\n"))
		end_angle=int(raw_input("Enter the ending angle of ellipse:\n"))
		color=raw_input("Enter color in red/blue/green/white: \n")
		temp_img=cv2.ellipse(img,(x1,y1),(a,b),angle,start_angle,end_angle,color_to_bgr(color),-1)
		cv2.imshow("Ellipse",temp_img)
		cv2.waitKey(0)
		cv2.destroyAllWindows()

	#	To Put the text on image		
	elif(choice==6):
		data=raw_input("Enter the string:\n")
		print "Enter the coordinates of the bottom left corner:\n"
		x1,y1=int(raw_input("x:  ")),int(raw_input("y:  "))
		color=raw_input("Enter color in red/blue/green/white: \n")
		font = cv2.FONT_HERSHEY_SIMPLEX
		temp_img=cv2.putText(img,data,(x1,y1),font,1,color_to_bgr(color),2)
		cv2.imshow("Text",temp_img)
		cv2.waitKey(0)
		cv2.destroyAllWindows()

	#	To save changes
	elif(choice==7):
		file_name=raw_input("Enter file name with location: ")		
		cv2.imwrite(file_name,temp_img)
		break

	#	OtherWise	
	else:
		break
		

