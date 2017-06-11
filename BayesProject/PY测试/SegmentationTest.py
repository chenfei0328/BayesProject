# -*- coding: utf-8 -*-

import unittest

class SegmentationTestCase(unittest.TestCase):
	def setUp(self):
		self.fenci = FenCi('the fenci')

	def tearDown(self):
		self.fenci.dispose()
		self.fenci = None

	def testSegmentationResult(self):
		"""Check that the Cate_prob are calculated correctly"""
		assert self.fenci.input('我爱上海') == ('我', '爱', '上海'), 'wrong result'

suite = unittest.makeSuite(SegmentationTestCase, 'test')