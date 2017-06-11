# -*- coding: utf-8 -*-
#!/usr/bin/python2.7

import sys
import getopt
import Segmentation as seg
import VectorSpaceModel as vsm
import Bayes as by

reload(sys)
sys.setdefaultencoding('utf-8')

class Entrance(by.NBayes):
	def __init__(self):
		super(Entrance, self).__init__()
	def input(self):
		self.initForUse()
		words = ''	 
		while words != 'q':
			words = raw_input('input:')
			self.predictForUse(words)

	def receive(self, words):
		self.initForUse()
		self.predictForUse(words)
		
def construction():
	try:
		s = seg.Segmentation()
		s.segmentation()

		b = by.NBayes()
		b.initForTest()
	except Exception, e:
		raise		
		
	print 'construction finished'

# options,args = getopt.getopt(sys.argv[1:], "", ["caption=","proc_name="])  
# if options != []:  
# 	for name,value in options:  
# 	    if name == '--caption':  
# 	        CAPTION = value
# 	        #e.receive(CAPTION)
# 	        print value
# 	    # if name == '--proc_name':  
# 	    #     PROC_NAME = value
# 	    #     print value



if __name__ == '__main__':
	
	# construction()
	e = Entrance()
	e.input()



	
	# s = 'wkjfghkj'
	# e = Entrance()
	# e.receive(s)

	# e = Entrance()

# 	options,args = getopt.getopt(sys.argv[1:], "", ["caption=","proc_name="])  
# 	if options != []:  
# 	    for name,value in options:  
# 	        if name == '--caption':  
# 	            CAPTION = value
# 	            # e.receive(CAPTION)
# 	            print value
# 	        # if name == '--proc_name':  
# 	        #     PROC_NAME = value
# 	        #     e.receive(PROC_NAME)