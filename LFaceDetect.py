import numpy as np
import cv2
from LVector import LVector
from lrect import LRect

#Face detector object
class LukesFaceDetector:
	def __init__(self):
		#initialize resources
		self.fileLocation = 'resources/'
		self.faceCascade = cv2.CascadeClassifier(self.fileLocation+'haarcascade_frontalface_default.xml')
		self.eyeCascade = cv2.CascadeClassifier(self.fileLocation+'haarcascade_eye.xml')
		self.faces = []
		self.eyes = []
	def detectFaces(self, gray):
		self.faces = []
		faces = self.faceCascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,minSize=(30, 30),flags = cv2.cv.CV_HAAR_SCALE_IMAGE)
		for x,y,w,h in faces:
			self.faces.append(LRect(x,y,w,h))
	def detectEyes(self, gray):
		self.eyes = []
		for r in self.faces:
			roi_gray = gray[r.y:r.y+r.h, r.x:r.x+r.w]
			eyes = self.eyeCascade.detectMultiScale(roi_gray)
			for e in eyes:
				e[0] += r.x
				e[1] += r.y
				self.eyes.append(LRect(*list(e)))
	#detect faces and eyes
	def detect(self, im):
		gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
		self.detectFaces(gray)
		self.detectEyes(gray)
	#draw a rectangle
	def rect(self, img, r, col):
		cv2.rectangle(img,(r.x,r.y),(r.x+r.w,r.y+r.h),col,2)
	#draw faces on img
	def drawFaces(self, img):
		for r in self.faces:
			self.rect(img, r, (255, 0, 0))
	#draw eyes on img
	def drawEyes(self, img):
		for r in self.eyes:
			self.rect(img, r, (0, 255, 0))