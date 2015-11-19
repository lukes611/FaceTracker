"""
	Title			: lrect.py
	Description		: a rectangle object
	Author			: Luke Lincoln
	Language		: Python
"""

from LVector import LVector

class LRect:
	def __init__(self, x=0, y=0, w=0, h=0):
		self.x = x
		self.y = y
		self.w = w
		self.h = h
	def pos(self):
		return LVector(self.x, self.y)
	def wh(self):
		return LVector(self.w, self.h)
	def hwh(self):
		return LVector(self.w, self.h) * 0.5
	def center(self):
		return (self.pos()+self.wh()) / 2
	def toString(self):
		return '[x={0},y={1},width={2},height={3}]'.format(*self.toList())
	def __str__(self):
		return self.toString()
	def toList(self):
		return [self.x,self.y,self.w,self.h]
	def clone(self):
		return LRect(self.x,self.y,self.w,self.h)
	def setFromCenter(self, centerPoint):
		hp = self.hwh()
		self.x = centerPoint[0] - hp[0]
		self.y = centerPoint[1] - hp[1]
	def scaleWH(self, scalar):
		#scalar can be either an LVector or a number
		c = self.center()
		hwh = self.wh() * scalar
		self.w, self.h = hwh[0], hwh[1]
		self.setFromCenter(c)
	def interpolateTo(self, r2, t):
		c = self.center()
		wh = self.wh()
		c.interpolateTo(r2.center(), t)
		wh.interpolateTo(r2.wh(), t)
		self.w, self.h = wh[0], wh[1]
		self.setFromCenter(c)
		
		