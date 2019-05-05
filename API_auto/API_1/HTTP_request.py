# _*_ coding: utf_8 _*_
# @Time     : 2019/3/12
# @Author   : yuandian
# @Email    : 919839065@qq.com
# @file     : class_0312
from API_auto.API_1.config import ConfigParsers
import requests


class HttpRequests:
    def request(self, method, url, param=None, cookies=None, json=None):
        CP = ConfigParsers()
        url = CP.get("swich", "http") + url
        if method.upper() == 'GET':
            result = requests.get(url, param, cookies=cookies)
        elif method.upper() == 'POST':
            if json:
                result = requests.post(url, json=json, cookies=cookies)
            else:
                result = requests.post(url, data=param, cookies=cookies)
        elif method.upper() == 'PUT':
            result = requests.put(url, data=param, cookies=cookies)
        return result


ht = HttpRequests()


# if __name__ == '__main__':
#     url = "http://test.lemonban.com/futureloan/mvc/api/member/login"
#     param = {"mobilephone": "18668208114", "pwd": "123456"}
#     ht = HttpRequests().request("POST",url,param)
#     print(ht.text)