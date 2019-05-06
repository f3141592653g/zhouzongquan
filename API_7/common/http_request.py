# -*- coding:utf-8 _*-
""" 
@author:mongo
@time: 2018/12/17 
@email:3126972006@qq.com
@function： 
"""
import requests

from API_7.common.config import config


class HTTPRequest:
    """
    独立session，cookies需要自己传递
    使用这类的request方法去完成不同的HTTP请求，并且返回响应结果
    """

    def request(self, method, url, data=None, json=None, cookies=None):

        method = method.upper()  # 将method强制转成全大小

        if type(data) == str:
            data = eval(data)  # str转成字典

        if method == 'GET':
            resp = requests.get(url, params=data, cookies=cookies)  # resp 是Response对象
        elif method == 'POST':
            if json:
                resp = requests.post(url, json=json, cookies=cookies)
            else:
                resp = requests.post(url, data=data, cookies=cookies)
        else:
            resp = None
            print('UN-support method')

        return resp


class HTTPRequest2:
    """
        公共使用一个session, cookies自动传递
       使用这类的request方法去完成不同的HTTP请求，并且返回响应结果
    """

    def __init__(self):
        # 打开一个session
        self.session = requests.sessions.session()

    def request(self, method, url, data=None, json=None):
        method = method.upper()  # 将method强制转成全大小

        if type(data) == str:
            data = eval(data)  # str转成字典

        # 拼接URL
        url = config.get('api', 'pre_url') + url
        print('请求url:', url)
        print('请求data:', data)

        if method == 'GET':
            resp = self.session.request(method=method, url=url, params=data)
        elif method == 'POST':
            if json:
                resp = self.session.request(method=method, url=url, json=json)
            else:
                resp = self.session.request(method=method, url=url, data=data)
        else:
            resp = None
            print('UN-support method')

        print('请求response:', resp.text)
        return resp

    def close(self):
        self.session.close()  # 用完记得关闭，很关键！！！


if __name__ == '__main__':
    # params = {"mobilephone": "15810447878", "pwd": "123456"}
    # http_request = HTTPRequest()
    # # 调用登陆
    # resp = http_request.request('pOST', 'http://test.lemonban.com/futureloan/mvc/api/member/login', data=params)
    # print(resp.status_code)
    # print(resp.text)
    # print(resp.cookies)
    #
    # # 调用充值
    # params = {"mobilephone": "15810447878", "amount": "1000"}
    # resp2 = http_request.request('POST', 'http://test.lemonban.com/futureloan/mvc/api/member/recharge', data=params,
    #                              cookies=resp.cookies)
    # print(resp2.status_code)
    # print(resp2.text)
    # print(resp2.cookies)

    http_request2 = HTTPRequest2()
    params = {"mobilephone": "15810447878", "pwd": "123456"}
    resp = http_request2.request('pOST', 'http://test.lemonban.com/futureloan/mvc/api/member/login', data=params)
    params = {"mobilephone": "15810447878", "amount": "1000"}
    resp2 = http_request2.request('POST', 'http://test.lemonban.com/futureloan/mvc/api/member/recharge', data=params)
    http_request2.close()
    print(resp2.status_code)
    print(resp2.text)
    print(resp2.cookies)
