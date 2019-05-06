# -*- coding:utf-8 _*-
""" 
@author:mongo
@time: 2018/12/17 
@email:3126972006@qq.com
@function： 
"""
import unittest

from ddt import ddt, data

from API_4.common import contants
from API_4.common import do_excel
from API_4.common.http_request import HTTPRequest2


@ddt
class RechargeTest(unittest.TestCase):
    excel = do_excel.DoExcel(contants.case_file, 'recharge')
    cases = excel.get_cases()

    @classmethod
    def setUpClass(cls):
        cls.http_request = HTTPRequest2()

    @data(*cases)
    def test_recharge(self, case):
        print(case.title)
        resp = self.http_request.request(case.method, case.url, case.data)
        actual_code = resp.json()['code']
        try:
            self.assertEqual(str(case.expected), actual_code)
            self.excel.write_result(case.case_id + 1, resp.text, 'PASS')
        except AssertionError as e:
            self.excel.write_result(case.case_id + 1, resp.text, 'FAIL')
            raise e

    @classmethod
    def tearDownClass(cls):
        cls.http_request.close()
