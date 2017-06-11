# -*- coding: utf-8 -*-

import unittest

class BayesTestCase(unittest.TestCase):
	def setUp(self):
		self.bayes = Nbayes('the bayes')

	def tearDown(self):
		self.bayes.dispose()
		self.bayes = None

	def testBayesResult(self):
		"""Check that the words are classified correctly"""
		testWord = ['我', '爱', '中国']
		assert self.bayes.input(testWord) == '1', 'wrong class'

suite = unittest.makeSuite(SegmentationTestCase, 'test')