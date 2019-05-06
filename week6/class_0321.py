# _*_ coding: utf_8 _*_
# @Time     : 2019/3/12
# @Author   : yuandian
# @Email    : 919839065@qq.com
# @file     : class_0312

import unittest
from ddt import ddt,data,unpack
from week6.get_data import *


@ddt
class Test_case(unittest.TestCase):
    re = Get_date()

    @data(*re)
    @unpack
    def test_normal_1(self,login,url,param,expected):
        print(login)
        res=request(url,eval(param)).json()["msg"]
        print(res)
        self.assertEqual(expected,res)

