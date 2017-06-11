# -*- coding: utf-8 -*-
#!/usr/bin/python2.7

import sys
import jieba
import numpy as np
import VectorSpaceModel as vsm

reload(sys)
sys.setdefaultencoding('utf-8')

class NBayes(vsm.VSM):

	def __init__(self):
		super(NBayes, self).__init__()
		# P(yi)
		self.classProbability = {}
		# P(x|yi)
		self.conditionalProbability = 0

		self.testSet = 0		

	def initForTest(self):
		self.start()
		print 'bayes start...'

		self.createClaPro()
		self.createConPro()

		print 'bayes model finished'

		for index in range(10):
			index *= 5
			testData = self.trainSet[index]
			self.test2Vocab(testData)
			self.predictForTest(index)

	def initForUse(self):
		self.readClaPro()
		self.readConPrp()

	def createClaPro(self):
		labelSet = set(self.labels)
		for lable in labelSet:
			self.classProbability[lable] = float(self.labels.count(lable)) / float(len(self.labels))

		with open('claPro.txt', 'w') as f:
			for line in self.classProbability:
				f.write(str(line) + ':' + str(self.classProbability[line]) + '\n')

	def createConPro(self):
		self.conditionalProbability = np.zeros([len(self.classProbability), self.vocabLength])
		sumWeight = np.zeros([len(self.classProbability), 1])

		for index in range(self.docLength):
			self.conditionalProbability[self.labels[index]] += self.tf_idf[index]
			sumWeight[self.labels[index]] = np.sum(self.conditionalProbability[self.labels[index]])
		self.conditionalProbability /= sumWeight

		with open('conPro.txt', 'w') as f:
			for line in self.conditionalProbability:
				for word in line:
					f.write(str(word) + '\n')

	def test2Vocab(self, testData):	
		self.testSet = np.zeros([1, self.vocabLength])
		for word in testData:
			if word in self.vocabulary:
				self.testSet[0, self.vocabulary.index(word)] += 1
		# print sum(sum(self.testSet))

	def predictForTest(self, index):

		predValue = 0
		predClass = ''

		for (keyVect, keyClass) in zip(self.conditionalProbability, self.classProbability):
			# P(x|yi)P(yi)
			temp = np.sum(self.testSet * keyVect * self.classProbability[keyClass])

			if temp > predValue:
				predValue = temp
				predClass = keyClass
		
		for key in self.class_code:
			if self.class_code[key] == predClass:
				print 'trainSet[%d]>%s' %(index, key)

	def readClaPro(self):
		self.classProbability = {}
		with open('claPro.txt', 'r') as f:
			content = f.readlines()
			for line in content:
				line = line.strip()
				lable = line[0]
				value = float(line[2:])
				self.classProbability[lable] = value

	def readConPrp(self):
	 	with open('vocabulary.txt', 'r') as f:
			self.vocabulary = f.read().splitlines()
 			self.vocabLength = len(self.vocabulary)
		self.conditionalProbability = np.zeros([len(self.classProbability), self.vocabLength])

		with open('conPro.txt', 'r') as f:
	 		# 先保存读出来的内容，否则读第二次为空
	 		content = f.readlines()

	 		self.docLength = len(content) / self.vocabLength
	 		self.conditionalProbability = np.zeros([len(self.classProbability), self.vocabLength])

	 		num = 0
	 		for line in content:

	 			x = num / self.vocabLength
	 			y = num % self.vocabLength

	 			self.conditionalProbability[x,y] = line.strip()
		
	 			num += 1

	def predictForUse(self, words):

		testData = jieba.cut(words)
		self.test2Vocab(testData)
		predValue = 0
		predClass = 0

		for (keyVect, keyClass) in zip(self.conditionalProbability, self.classProbability):
			# P(x|yi)P(yi)
			temp = np.sum(self.testSet * keyVect * self.classProbability[keyClass])

			if temp > predValue:
				predValue = temp
				predClass = keyClass

		for key in self.class_code:
			if self.class_code[key] == int(predClass):
				#return key
				print '%s->%s' %(words, key)


if __name__ == '__main__':
	bayes = NBayes()
	bayes.initForTest()