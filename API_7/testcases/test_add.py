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
from API_7.common.config import config
from API_7.common import context
from API_7.common.http_request import HTTPRequest2


@ddt
class AddTest(unittest.TestCase):
    excel = do_excel.DoExcel(contants.case_file, 'add')
    cases = excel.get_cases()

    @classmethod
    def setUpClass(cls):
        cls.http_request = HTTPRequest2()

    @data(*cases)
    def test_add(self, case):
        # case.data = eval(case.data)  # 变成字典
        # print(type(case.data))
        # if case.data.__contains__('mobilephone') and case.data['mobilephone'] == 'normal_user':
        #     case.data['mobilephone'] = config.get('data', 'normal_user')  # 拿到配置文件里面的值赋值给mobilephone
        #
        # if case.data.__contains__('pwd') and case.data['pwd'] == 'normal_pwd':
        #     case.data['pwd'] = config.get('data', 'normal_pwd')  # 拿到配置文件里面的值赋值给mobilephone
        #
        # if case.data.__contains__('memberId') and case.data['memberId'] == 'loan_member_id':
        #     case.data['memberId'] = config.get('data', 'loan_member_id')  # 拿到配置文件里面的值赋值给mobilephone
        # 在请求之前替换参数化的值
        case.data = context.replace(case.data)
        resp = self.http_request.request(case.method, case.url, case.data)
        try:
            self.assertEqual(str(case.expected), resp.json()['code'])
            self.excel.write_result(case.case_id + 1, resp.text, 'PASS')
        except AssertionError as e:
            self.excel.write_result(case.case_id + 1, resp.text, 'FAIL')
            raise e

    @classmethod
    def tearDownClass(cls):
        cls.http_request.close()
