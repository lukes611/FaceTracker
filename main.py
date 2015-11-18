import numpy as np
import cv2
from LFaceDetect import LukesFaceDetector

cap = cv2.VideoCapture(0)

faceDetector = LukesFaceDetector()

while True:
	ret, frame = cap.read()
	
	faceDetector.detect(frame)
	
	faceDetector.drawFaces(frame)
	faceDetector.drawEyes(frame)
	
	cv2.imshow('frame', frame)
	if cv2.waitKey(30) == 27:
		break
	
cap.release()
cv2.destroyAllWindows()