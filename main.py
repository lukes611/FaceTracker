import numpy as np
import cv2
from LFaceDetect import LukesFaceDetector
from LVector import LVector
from lrect import LRect

'''
What to do:
1. face tracking rather than just searching:
	stores a current list,
	update matches to old faces if no match is found, else adds new ones with new ids
	
	feature/s detection and saving for faces
	database
	ability to add names to faces
	ability to connect over network
'''

v1 = LVector(5,2)
v2 = LVector(10,8)
print v1, v2
v1.interpolateTo(v2, 0.5)
print v1
'''
#init video capture object
cap = cv2.VideoCapture(0)

#create face detection object
faceDetector = LukesFaceDetector()


while True:
	#whilst user hasn't quit:
	
	#read frame
	ret, frame = cap.read()

	#detect faces
	faceDetector.detect(frame, True)
	
	#mark image with rectangles around faces and eyes
	faceDetector.draw(frame)
	
	#show user the augmented image
	cv2.imshow('frame', frame)
	if cv2.waitKey(30) == 27:
		break

#free resources		
cap.release()
cv2.destroyAllWindows()
'''