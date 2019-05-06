# -*- coding:utf-8 _*-
""" 
@author:mongo
@time: 2018/12/17 
@email:3126972006@qq.com
@function： 
"""

"""
两种传递cookie的方式
1，单独的session，把上一个请求的返回cookies，指定传递到下一个请求的入参cookie当中
2，使用同一个session，就会自动传递cookie。
"""

import requests

session = requests.sessions.session()
# 登陆
params = {"mobilephone": "15810447878", "pwd": "123456"}
resp = session.request('post',
                       url='http://test.lemonban.com/futureloan/mvc/api/member/login',
                       data=params)
print(resp.status_code)
print(resp.text)
print(resp.cookies)

# 充值
# session2 = requests.sessions.session()
params = {"mobilephone": "15810447878", "amount": "1000"}
resp = session.request('post',
                       url='http://test.lemonban.com/futureloan/mvc/api/member/recharge',
                       data=params)
print(resp.status_code)
print(resp.text)
print(resp.cookies)

session.close()  # session关闭
