import numpy as np
import cv2
from LFaceDetect import LukesFaceDetector
from LVector import LVector

'''
What to do:
1. face tracking rather than just searching
	need colors based on id
	vector obj
	rect obj
	feature/s detection and saving for faces
	database
	ability to add names to faces
	ability to connect over network
'''
a = LVector(1,2,3)
b = LVector(2,4,0)
c = LVector(2, 6, 0)
print c.dist(b), b.dist(c), a.dist(b)
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
	faceDetector.detect(frame)
	
	#mark image with rectangles around faces and eyes
	faceDetector.drawFaces(frame)
	faceDetector.drawEyes(frame)
	
	#show user the augmented image
	cv2.imshow('frame', frame)
	if cv2.waitKey(30) == 27:
		break

#free resources		
cap.release()
cv2.destroyAllWindows()
'''