# _*_ coding: utf_8 _*_
# @Time     : 2019/3/12
# @Author   : yuandian
# @Email    : 919839065@qq.com
# @file     : class_0312
import sys
import unittest
from API_auto.API_1 import test_case
import HTMLTestRunnerNew

print(sys.path)
sys.path.append('./')

suite = unittest.TestSuite()
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromModule(test_case))

with open("test.html", "wb") as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file, verbosity=2, title='3月28日测试报告',
                                              description='这是一个测试正常值和异常值的测试报告', tester='原点')
    runner.run(suite)
