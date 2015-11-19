"""
	Title			: LFace.py
	Description		: an object representing faces
	Author			: Luke Lincoln
	Language		: Python
"""
from LVector import LVector
from lrect import LRect

class LFace:
	def __init__(self, faceRect=LRect(), eyes=[], id = 0):
		self.face = faceRect.clone()
		self.eyes = [e.clone() for e in eyes]
		self.id = id
	def clone(self):
		return LFace(self.face, self.eyes, self.id)
	def dist(self, f2, scalar1 = 1.0, scalar2 = 0.2):
		#distance is defined as: center differences * scalar1 + size differences * scalar2
		d1 = self.face.center().dist(f2.face.center())
		d2 = self.face.wh().dist(f2.face.wh())
		return d1 * scalar1 + d2 * scalar2
	def interpolateTo(self, f2, t):
		self.face.interpolateTo