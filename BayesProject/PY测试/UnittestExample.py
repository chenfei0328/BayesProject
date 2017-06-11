# -*- coding: utf-8 -*-

import unittest

class WidgetTestCase(unittest.TestCase):

    #测试框架会在运行测试时自动调用
    def setUp(self):
		self.widget = Widget("The widget")

	#完成在runTest运行之后的清理工作
	def tearDown(self):
		self.widget.dispose()
		self.widget = None

	def testDefaultSize(self):
		assert self.widget.size() == (50,50), 'incorrect default size'
    def testResize(self):
		self.widget.resize(100,150)
		assert self.widget.size() == (100,150), \
	       'wrong size after resize'

#测试某些功能组成的套件
def suite():
   suite = unittest.TestSuite()
   suite.addTest(WidgetTestCase("testDefaultSize"))
   suite.addTest(WidgetTestCase("testResize"))
   return suite
#或者如下   
class WidgetTestSuite(unittest.TestSuite):
   def __init__(self):
       	unittest.TestSuite.__init__(self,map(WidgetTestCase,
					     ("testDefaultSize",
					      "testResize")))

#测试所有的测试用例组成的测试套件
suite = unittest.makeSuite(WidgetTestCase,'test')