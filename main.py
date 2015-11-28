import numpy as np
import cv2
from LFaceDetect import LukesFaceDetector
from LVector import LVector
from lrect import LRect
from LFaceTracker import LukesFaceTracker
import sys
import os

'''
What to do:
1. face tracking rather than just searching:
	feature/s detection and saving for faces
	database
	ability to add names to faces
	ability to connect over network
'''


cap = None

#init video capture object
#from webcam
#or from video
if len(sys.argv) <= 1:
	cap = cv2.VideoCapture(0)
elif os.path.isfile(sys.argv[1]):
	cap = cv2.VideoCapture(sys.argv[1])
else:
	print 'error, cannot find specified file:', sys.argv[1]
	sys.exit(5)

#create face detection object
faceDetector = LukesFaceDetector()
faceTracker = LukesFaceTracker()


while True:
	#whilst user hasn't quit:
	
	#read frame
	ret, frame = cap.read()
	if not ret:
		print 'Cannot gain access to web cam'
		break
	
	#detect faces
	faceDetector.detect(frame, True)
	faceTracker.update(faceDetector.faces)
	
	#mark image with rectangles around faces and eyes
	faceTracker.draw(frame)
	
	#show user the augmented image
	cv2.imshow('frame', frame)

	key = cv2.waitKey(30)

	if key in [27, 1048603]:
		break
	

#free resources		
cap.release()
cv2.destroyAllWindows()
