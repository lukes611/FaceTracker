"""
	Title			: LFaceTracker.py
	Description		: an object which tracks faces
	Author			: Luke Lincoln
	Language		: Python
"""
import numpy as np
import cv2
from LVector import LVector
from lrect import LRect
from LFace import LFace
from colorlist import ColorList

class LukesFaceTracker:
	def __init__(self):
		self.colors = ColorList(100)
		self.idCount = 0
		self.faces = []
	def newId(self):
		rv = self.idCount
		self.idCount += 1
		return rv
	def colorById(self, id):
		id %= self.colors.size()
		return self.colors[id]
	def update(self, newFaces):
		print self.idCount
		toAdd = [True] * len(newFaces)
		for i, f in enumerate(self.faces):
			v = f.update(newFaces, 4)
			if v != -1:
				toAdd[v] = False
		for i, f in enumerate(newFaces):
			if toAdd[i]:
				nf = f.clone()
				nf.id = self.newId()
				self.faces.append(nf)
	def rect(self, img, r, col):
		cv2.rectangle(img,(int(r.x),int(r.y)),(int(r.x+r.w),int(r.y+r.h)),col,2)
	#draw faces on img
	def draw(self, img):
		for f in self.faces:
			self.rect(img, f.face, (255, 0, 0))
	