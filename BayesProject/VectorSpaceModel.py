# -*- coding: utf-8 -*-
#!/usr/bin/python2.7

import sys
import os
import numpy as np
import Segmentation as seg

reload(sys)
sys.setdefaultencoding('utf-8')

class VSM(seg.Path):

	class_code = {'art' : 0, 'computer' : 1, 'economic' : 2, \
		'education' : 3, 'environment' : 4, 'medical' : 5 , \
		'military' : 6, 'politics' : 7, 'sports' : 8, 'traffic' : 9}

	def __init__(self):
		super(VSM, self).__init__()
		# seg.Path.__init__(self)

		# 词典
		self.vocabulary = []
		# 停用词表
		self.stop_word_list = []

		# 所有文档
		self.trainSet = []
		# 文档对应的类别
		self.labels = []
		
		# 导入的trainSet文档数
		self.docLength = 0
		# 词汇表词数
		self.vocabLength = 0		

		self.tf = 0

		self.idf = 0
		self.tf_idf = 0

	def start(self):
		print 'VSM start...'
		self.loadTrainSet()
		self.createVocabulary()
		self.bagOfWords2Vec()
		self.createTF_IDF()
		print 'VSM finished'

	# 加载数据集
	def loadTrainSet(self):
		for class_path in self.all_new_class_path:
			doc_list = os.listdir(class_path)
			for doc in doc_list:
				self.labels.append(self.class_code[class_path[14:-1]])
				full_path = class_path + doc
				with open(full_path, 'r') as f:
					content = f.read().strip().split()

					self.trainSet.append(content) #添加的不是中文
					#self.trainSet.append(''.join(content))			
					self.vocabulary.extend(content)	
	
	# 建立词典				
	def createVocabulary(self):
		vocabSet = set([])

		for word in self.vocabulary:
			vocabSet.add(word)	

		with open(self.stop_word_path, 'r') as f:
			self.stop_word_list = f.read().splitlines()

		# 删除停用词表中的词
		vocabSet = vocabSet - set(self.stop_word_list)
		self.vocabulary = list(vocabSet)

		# 写入文件，持久化
		with open('vocabulary.txt', 'w') as f:
			for word in self.vocabulary:
				f.write(word + '\n')

	# 建立词袋模型
	def bagOfWords2Vec(self):
		self.vocabLength = len(self.vocabulary)
		self.docLength = len(self.trainSet)
		self.tf = np.ones([self.docLength, self.vocabLength])

		for index in range(self.docLength):
			for word in self.trainSet[index]:
				if word in self.vocabulary:
					self.tf[index, self.vocabulary.index(word)] += 1
    
    # 建立tf-idf模型
	def createTF_IDF(self):
		self.idf = np.ones([1,self.vocabLength])
		self.tf_idf = np.ones([self.docLength, self.vocabLength])
		for index in range(self.docLength):
			self.tf[index] /= float(sum(self.tf[index]))
			for word in set(self.trainSet[index]):
				if word in self.vocabulary:
					self.idf[0, self.vocabulary.index(word)] += 1
		
		self.idf = np.log(float(self.docLength) / self.idf)
		self.tf_idf = np.multiply(self.tf, self.idf)

		print len(self.tf_idf)
		# 写入文件，持久化
		with open('tf_idf.txt', 'w') as f:
			for line in self.tf_idf:
				for word in line:
					f.write(str(word) + '\n')


if __name__ == '__main__':
	vsm = VSM()
	# vsm.start()