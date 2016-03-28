import numpy as np
import cv2
from LFaceDetect import LukesFaceDetector
from LVector import LVector
from lrect import LRect
from LFaceTracker import LukesFaceTracker
from LFDB import LFDB
import sys
import os
import random

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
db = LFDB()
doCap = False

print db.db

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
	if not doCap:
		faceTracker.draw(frame)
	else:
		for i, f in enumerate(faceTracker.faces):
			r = f.face
			fim = np.copy(frame[r.y:r.y+r.h, r.x:r.x+r.w])
			db.add(fim, 'jun')
		doCap = False
	#show user the augmented image
	cv2.imshow('frame', frame)

	key = cv2.waitKey(30)

	if key in [27, 1048603]:
		break
	if key == 99:
		doCap = True
	if key != -1: print key

	
	
for i in db.faces:
	im = db.getIm(i)
	cv2.imshow('a', im)
	cv2.waitKey()
#free resources		
cap.release()
cv2.destroyAllWindows()
