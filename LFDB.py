import os
import cv2
import numpy as np

'''
format: name.number.png
unknown: unknown.number.png

faces is indexed by name.number
'''

class LFDB:
	def __init__(self):
		self.dir = './resources/db/'
		self.db = self.load()
		self.faces = {}
	def load(self):
		return ['.'.join(f.split('.')[0:-1]) for f in os.listdir(self.dir)]
	def getNames(self): return set([i.split('.')[0] for i in self.db])
	def getByName(self, name): return [i for i in self.db if i.split('.')[0] == name]
	def nextNumber(self, name):
		l = [int(i.split('.')[-1]) for i in self.getByName(name)]
		return 0 if len(l) == 0 else max(l)+1
	def add(self, f, name='unknown'):
		nn = name + '.' + str(self.nextNumber(name))
		self.db.append(nn)
		self.faces[nn] = f
		cv2.imwrite(self.dir + nn + '.png', self.faces[nn])
	def getIm(self, n):
		if n not in self.faces:
			i = cv2.imread(self.dir+n+'.png', cv2.IMREAD_GRAYSCALE)
			self.faces[n] = cv2.resize(i,(160, 160), interpolation = cv2.INTER_CUBIC)
		return self.faces[n]
	def trainingData(self):
		fc, labs, labConversion = [], [], []
		for i in self.db:
			fc.append(self.getIm(i))
			labs.append(i.split('.')[0])
		labConversion = list(set(labs))
		labs = [labConversion.index(i) for i in labs]
		return fc, np.array(labs), labConversion
			