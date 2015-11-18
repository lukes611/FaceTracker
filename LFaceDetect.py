import numpy as np
import cv2

class LukesFaceDetector:
	def __init__(self):
		self.fileLocation = 'C:/Users/luke/Documents/ocv3a/ocvbinaries/install/etc/haarcascades/'
		self.faceCascade = cv2.CascadeClassifier(self.fileLocation+'haarcascade_frontalface_default.xml')
		self.eyeCascade = cv2.CascadeClassifier(self.fileLocation+'haarcascade_eye.xml')
		self.faces = []
		self.eyes = []
	def detect(self, im):
		gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
		self.faces = self.faceCascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,minSize=(30, 30),flags = cv2.cv.CV_HAAR_SCALE_IMAGE)
		self.eyes = []
		for x,y,w,h in self.faces:
			roi_gray = gray[y:y+h, x:x+w]
			eyes = self.eyeCascade.detectMultiScale(roi_gray)
			for i in range(len(eyes)):
				eyes[i][0] += x
				eyes[i][1] += y
			self.eyes.extend(eyes)
	
	def rect(self, img, x, y, w, h, col):
		cv2.rectangle(img,(x,y),(x+w,y+h),col,2)
	def drawFaces(self, img):
		for x,y,w,h in self.faces:
			self.rect(img, x, y, w, h, (255, 0, 0))
	def drawEyes(self, img):
		for x,y,w,h in self.eyes:
			self.rect(img, x, y, w, h, (0, 255, 0))