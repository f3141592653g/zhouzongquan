# _*_ coding: utf_8 _*_
# @Time     : 2019/3/12
# @Author   : yuandian
# @Email    : 919839065@qq.com
# @file     : class_0312

import requests


class Request:
    def request(self, url, param, method="GET"):
        if method.upper() == 'GET':
            result = requests.get(url, param)
        elif method.upper() == 'POST':
            result = requests.get(url, param)
        return result


if __name__ == '__main__':

    url="http://47.107.168.87:8080/futureloan/mvc/api/member/login"
    param={'mobilephone':'18688773467','pwd':''}
    result=Request().request(url,param).json()["msg"]
    print(result)

