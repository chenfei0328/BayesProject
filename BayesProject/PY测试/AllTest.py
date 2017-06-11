# -*- coding: utf-8 -*-

import unittest
import SegmentationTest
import WordFrequencyVectorTest
import BayesTest

#测试方法一：命令行执行本脚本，本函数自动执行所有以test*命名的测试用例
if __name__ == '__main__':
	unittest.main()

#测试方法二：命令行执行本脚本，参数为待测试的套件名，如下四个实例
suite1 = SegmentationTest.TheTestSuite()
suite2 = WordFrequencyVectorTest.TheTestSuite()
suite3 = BayesTest.TheTestSuite()

alltests = unittest.TestSuite((suite1, suite2, suite3))