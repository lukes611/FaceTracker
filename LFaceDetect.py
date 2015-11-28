"""
	Title			: LFaceDetect.py
	Description		: an object used to detect faces
	Author			: Luke Lincoln
	Language		: Python
"""

import numpy as np
import cv2
from LVector import LVector
from lrect import LRect
from LFace import LFace
from colorlist import ColorList

#Face detector object
class LukesFaceDetector:
	def __init__(self):
		#initialize resources
		self.fileLocation = 'resources/'
		self.faceCascade = cv2.CascadeClassifier(self.fileLocation+'haarcascade_frontalface_default.xml')
		self.eyeCascade = cv2.CascadeClassifier(self.fileLocation+'haarcascade_eye.xml')
		self.faces = []
		self.colors = ColorList(100)
	def detectFaces(self, gray):
		self.faces = []
		faces = self.faceCascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,minSize=(5, 5))
		for x,y,w,h in faces:
			self.faces.append(LFace(LRect(x,y,w,h)))
	def detectEyes(self, gray):
		self.eyes = []
		for f in self.faces:
			r = f.face
			roi_gray = gray[r.y:r.y+r.h, r.x:r.x+r.w]
			eyes = self.eyeCascade.detectMultiScale(roi_gray)
			for e in eyes:
				e[0] += r.x
				e[1] += r.y
				f.eyes.append(LRect(*list(e)))
	#detect faces and eyes
	def detect(self, im, skipEyes = False):
		gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
		self.detectFaces(gray)
		if not skipEyes:
			self.detectEyes(gray)
	#draw a rectangle
	def rect(self, img, r, col):
		cv2.rectangle(img,(r.x,r.y),(r.x+r.w,r.y+r.h),col,2)
	#draw faces on img
	def drawFaces(self, img):
		for f in self.faces:
			self.rect(img, f.face, (255, 0, 0))
	#draw eyes on img
	def drawEyes(self, img):
		for f in self.faces:
			for e in f.eyes:
				self.rect(img, e, (0, 255, 0))
	def draw(self, img):
		for i,f in enumerate(self.faces):
			self.rect(img, f.face, self.colors[i])
			for e in f.eyes:
				self.rect(img, e, self.colors[i])