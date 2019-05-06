# -*- coding:utf-8 _*-
""" 
@author:mongo
@time: 2018/12/17 
@email:3126972006@qq.com
@function： 
"""
import unittest

from ddt import ddt, data

from API_7.common import contants
from API_7.common import do_excel
from API_7.common.http_request import HTTPRequest2


@ddt
class LoginTest(unittest.TestCase):
    excel = do_excel.DoExcel(contants.case_file, 'login')
    cases = excel.get_cases()

    @classmethod
    def setUpClass(cls):
        cls.http_request = HTTPRequest2()

    @data(*cases)
    def test_login(self, case):
        resp = self.http_request.request(case.method, case.url, case.data)

        try:
            self.assertEqual(case.expected, resp.text)
            self.excel.write_result(case.case_id + 1, resp.text, 'PASS')
        except AssertionError as e:
            self.excel.write_result(case.case_id + 1, resp.text, 'FAIL')
            raise e

    @classmethod
    def tearDownClass(cls):
        cls.http_request.close()
