# _*_ coding: utf_8 _*_
# @Time     : 2019/3/12
# @Author   : yuandian
# @Email    : 919839065@qq.com
# @file     : class_0312

# 1,扩展之前实现好的http_request，支持传cookies
# 2，完成接口文档中注册，登录，充值的调用
# 3，熟悉之前发给你们的接口文档和需求介绍视频，做个每个接口功能了然于心！！！

import requests


class Request:

    cookies = result_2.cookies

    # 注册
    def register(self, url, data):
        result = requests.post(url, data)
        return result

    # 登录
    def login(self, url, data):
        result_2 = requests.post(url, data)
        return result_2

    # 充值
    def recharge(self, url, data):
        result_3 = requests.post(url, data,cookies=result_2.cookies)
        return result_3


if __name__ == '__main__':

    url_1 = "http://test.lemonban.com/futureloan/mvc/api/member/register"
    url_2 = "http://test.lemonban.com/futureloan/mvc/api/member/login"
    url_3 = "http://test.lemonban.com/futureloan/mvc/api/member/recharge"
    data = {"mobilephone": "18668208113", "pwd": "123456"}

    result_1 = Request().register(url_1, data).text
    print(result_1)

    result_2 = Request().login(url_2, data)
    print(result_2.text)

    result_3 = Request().recharge(url_3, data).text
    print(result_3)