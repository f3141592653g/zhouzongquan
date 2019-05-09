# _*_ coding: utf_8 _*_
# @Time     : 2019/3/12
# @Author   : yuandian
# @Email    : 919839065@qq.com
# @file     : class_0312

import unittest
from ddt import ddt, data, unpack
from API_auto.API_1.get_data import *
from API_auto.API_1.HTTP_request import *
from API_auto.API_1.regular import Regular
from API_auto.API_1 import do_mysql
from API_auto.API_1.logger_msg import *

COOKIES = None


@ddt
class Test_case(unittest.TestCase):
    re = DoExcel().Get_date()

    @classmethod
    def setUpClass(cls):
        cls.http_request = HttpRequests()
        cls.mysql = do_mysql.DoMysql()
        cls.logger = Logger("py15").log()

    @data(*re)
    @unpack
    def test_normal_1(self, case_id, title, method, url, data, expected, sql):
        global COOKIES
        data = Regular().context(data)
        sql = Regular().context(str(sql))
        # if data.find("normal_user") > 1:
        #     sql = 'select max(mobilephone) from future.member'
        #     max_phone = int(self.mysql.sel_one(sql)[0])+1
        #     print("最大手机号码：", max_phone)
        #     data = data.replace('register_mobile', str(max_phone))  # 替换
        self.logger.debug("==============正在执行{}的测试用例==============".format(title))
        self.logger.info("data:{}".format(data))
        if title == "正常充值":
            recharge_sql = sql
            recharge_before = self.mysql.sel_one(recharge_sql)[0]
            self.logger.debug("充值前的金额是：{}".format(recharge_before))
        if title == "竞标成功":
            add_sql = sql
            add_before = self.mysql.sel_one(add_sql)[0]
            self.logger.debug("竞标前的金额是：{}".format(add_before))

        actuel = ht.request(method, url, eval(data), cookies=COOKIES)
        DoExcel().write_data(actuel, case_id=case_id)
        if actuel.cookies:
            COOKIES = actuel.cookies
            res = actuel.json()["msg"]
            DoExcel().write_data(actuel, case_id=case_id)
            self.logger.info("预期结果是：{}".format(expected))
            self.logger.info("实际结果是：{}".format(res))
        else:
            res = actuel.json()["msg"]
            DoExcel().write_data(actuel, case_id=case_id)
            self.logger.info("预期结果是：{}".format(expected))
            self.logger.info("实际结果是：{}".format(res))
        try:
            self.assertEqual(expected, res)
            if actuel.json()['msg'] == "注册成功" or actuel.json()['msg'] == "登录成功" or actuel.json()['msg'] == "手机号码已被注册":
                if sql is not None:
                    memer_id = self.mysql.sel_one(sql)[0]
                    self.logger.info("用户ID：{}".format(memer_id))
                    # 保存到类属性里面
                    setattr(Regular, "memer_id", str(memer_id))
                    self.logger.info("memer_id是否存入进去了：{}".format(hasattr(Regular, "memer_id")))
            elif actuel.json()['msg'] == "充值成功":
                recharge_sql = sql
                recharge_after = self.mysql.sel_one(recharge_sql)[0]
                self.logger.debug('充值之后的金额是：{}'.format(recharge_after))
                self.assertEqual(recharge_before, int(recharge_after)-100)

            elif actuel.json()['msg'] == "竞标成功":
                add_sql = sql
                add_after = self.mysql.sel_one(add_sql)[0]
                self.logger.critical("竞标之后的金额是：{}".format(add_after))
                self.assertEqual(add_before, int(add_after)+100)
            self.logger.info("=============={}用例执行完毕=============".format(title))
        except AssertionError as e:
            raise e

    @classmethod
    def tearDownClass(cls):
        cls.mysql.sel_close()
