"""
	Title			: LFace.py
	Description		: an object representing faces
	Author			: Luke Lincoln
	Language		: Python
"""
from LVector import LVector
from lrect import LRect

class LFace:
	def __init__(self, faceRect=LRect(), eyes=[], id = 0, mt = 0, vel = LVector(0,0)):
		self.face = faceRect.clone()
		self.eyes = [e.clone() for e in eyes]
		self.id = id
		self.missingTicks = mt
		self.velocity = vel
	def clone(self):
		return LFace(self.face, self.eyes, self.id)
	def setAs(self, f2):
		self.face = f2.face.clone()
		self.eyes = [e.clone() for e in f2.eyes]
		self.id = f2.id
		self.missintTicks = f2.missingTicks
		self.velocity = f2.velocity.clone()
	def dist(self, f2, scalar1 = 1.0, scalar2 = 0.2):
		#distance is defined as: center differences * scalar1 + size differences * scalar2
		d1 = self.face.center().dist(f2.face.center())
		d2 = self.face.wh().dist(f2.face.wh())
		return d1 * scalar1 + d2 * scalar2
	def interpolateTo(self, f2, t):
		self.face.interpolateTo(f2.face, t)
		self.eyes = f2.clone().eyes if t > 0.5 else []
	def getPredicted(self):
		rv = self.clone()
		p = rv.face.center()
		oldP = p.clone()
		p += self.velocity
		rv.velocity = LVector(0,0)
		rv.face.setFromCenter(p)
		return rv
	def update(self, newFaces, maxDist = 90.0):
		#checks for possible, matches, if match found: returns index else -1 
		match = [0,0]
		isSet = False
		for i, f in enumerate(newFaces):
			cost = self.dist(f)
			if cost > maxDist: continue
			if (isSet and cost < match[0]) or not isSet:
				match = [cost, i]
				isSet = True
		if not isSet:		
			self.missingTicks+=1
			self.velocity *= 0
			return -1
		t = 1 - (match[0] / maxDist)
		self.missingTicks = 0
		predicted = self.getPredicted()
		predicted.interpolateTo(newFaces[match[1]], t)
		self.setAs(predicted)
		return match[1]