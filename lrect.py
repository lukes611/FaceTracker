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
	def avg(self):
		return (self.pos()+self.wh()) / 2
	def toString(self):
		return '[x={0},y={1},width={2},height={3}]'.format(*self.toList())
	def __str__(self):
		return self.toString()
	def toList(self):
		return [self.x,self.y,self.w,self.h]