import numpy as np
import cv2
from LFaceDetect import LukesFaceDetector

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