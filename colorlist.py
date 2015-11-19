"""
	Title			: colorlist.py
	Description		: a colorlist object can generate colors for use as ids
	Author			: Luke Lincoln
	Language		: Python
"""
from random import random

class ColorList:
	def __init__(self, count = 50):
		self.colors = [self.randomColor(255) for i in range(count)]
	def randomColor(self, scalar=255):
		return (self.rand(scalar), self.rand(scalar), self.rand(scalar))
	def rand(self, scalar):
		return random() * scalar + (255-scalar)
	def __getitem__(self, index):
		return self.colors[index]
	def size(self):
		return len(self.colors)