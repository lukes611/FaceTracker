"""
	Title			: LVector.py
	Description		: an n-dimensional vector object
	Author			: Luke Lincoln
	Language		: Python
"""

import math

class LVector:
	def __init__(self, *args):
		self.data = [x for x in args]
	def toString(self):
		return str(self.data)
	def __str__(self):
		return self.toString()
	def filter(self, f):
		self.data = [f(x) for x in self.data]
	def filterClone(self, f):
		rv = self.clone()
		rv.filter(f)
		return rv
	def size(self):
		return len(self.data)
	def __add__(self, v2):
		return self.combineFilterClone(v2, lambda x, y : x + y)
	def __sub__(self, v2):
		return self.combineFilterClone(v2, lambda x, y : x - y)
	def __mul__(self, v2):
		if isinstance(v2,LVector):
			return self.combineFilterClone(v2, lambda x, y : x * y)
		else:
			return self.filterClone(lambda x: x * v2)
	def __div__(self, v2):
		return self.filterClone(lambda x: x / v2)
	def mag(self):
		return math.sqrt(self.dot(self))
	def dist(self, v2):
		return (self.__sub__(v2)).mag()
	def dot(self, v2):
		return (self.__mul__(v2).sum())
	def sum(self):
		rv = 0
		for i in self.data : rv += i
		return rv
	def clone(self):
		return LVector(*self.data)
	#set each element of self x based on lambda f and element y of v2 so x = f(x,y)
	def combineFilter(self, v2, f):
		assert self.size() == v2.size(), 'adding two vectors with different lengths'
		for i in range(self.size()): self.data[i] = f(self.data[i],v2.data[i])
	def combineFilterClone(self, v2, f):
		assert self.size() == v2.size(), 'adding two vectors with different lengths'
		rv = self.clone()
		for i in range(rv.size()): rv.data[i] = f(rv.data[i],v2.data[i])
		return rv
	def __getitem__(self, index):
		return self.data[index]
	def __setitem__(self, index, value):
		self.data[index] = value
		