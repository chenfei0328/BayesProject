# -*- coding: utf-8 -*-

import unittest

class WFVTestCase(unittest.TestCase):
	def setUp(self):
		self.wfv = WFV('the wfv')

	def tearDown(self):
		self.wfv.dispose()
		self.wfv = None

	def testCate_prob(self):
		"""Check that the Cate_prob are calculated correctly"""
		classVec = [1, 0, 1, 0, 1]
		self.wfv.Cate_prob(classVec)
		assert self.wfv.Pcates == {0 : 2/5, 1 : 3/5}, 'wrong pcates'

	def testCalc_tfidf(self):
		"""Check that the tf_idf are calculated correctly"""
		self.wfv.Calc_tfidf(testSet)
		assert self.wfv.tf = [], 'wrong tf'
		assert self.wfv.idf = [], 'wrong idf'
		assert self.wfv.tf_idf = [], 'wrong tf_idf'

	def testbuild_tdm(self):
		"""Check that the tdm are calculated correctly"""
		self.wfv.tf_idf = []
		self.wfv.build_tdm()
		assert self.wfv.tdm = [], 'wrong tdm'

suite = unittest.makeSuite(WFVTestCase, 'test')