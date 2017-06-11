#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import sys
import os
import jieba

reload(sys)
sys.setdefaultencoding('utf-8')

class Path(object):

	old_path = 'train_set_old/'
	new_path = 'train_set_new/'
	stop_word_path = 'stop_word_list/stop_word_list.txt'

	# art ...
	all_class_list = os.listdir(old_path)

	# 'train_set_old/art/' , ...
	all_old_class_path = []
	all_new_class_path = []

	def __init__(self):

		for class_path in self.all_class_list:

			old_doc_path = self.old_path + class_path + '/'
			new_doc_path = self.new_path + class_path + '/'

			self.all_old_class_path.append(old_doc_path)
			self.all_new_class_path.append(new_doc_path)			
			
			for new_class_path in self.all_new_class_path:						
				if not os.path.exists(new_class_path):
					os.makedirs(new_class_path)

# 分词
class Segmentation(Path):

	# 读文件
	def read_file(self, path):
		with open(path, 'r') as f:
			return f.read()

	# 写文件
	def save_file(self, path, content):
		with open(path, 'w') as f:
			f.write(content)

	# 结巴分词
	def segmentation(self):
		for (old_class_path, new_class_path) in zip(self.all_old_class_path, self.all_new_class_path):
			
			doc_list = os.listdir(old_class_path)
			
			for doc_path in doc_list:			
				content = self.read_file(old_class_path + doc_path).strip()
				content = content.replace('\n', '').replace(' ', '')

				# 结巴分词，默认精确模式
				content = jieba.cut(content)
				self.save_file(new_class_path + doc_path, ' '.join(content))

		print 'segmentation finished'

# if __name__ == '__main__':
# 	seg = Segmentation()
# 	seg.segmentation()	