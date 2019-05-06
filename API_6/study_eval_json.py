# -*- coding:utf-8 _*-
""" 
@author:mongo
@time: 2018/12/17 
@email:3126972006@qq.com
@function：  数据类型的转换 str-->dict
"""
import json

# 正常的json格式
# {"key":[]}
params = '{"status":1,"code":"10001","data":null,"msg":"登录成功"}'  # 返回
p = '{"mobilephone":"15810447878","pwd":None}'  # 请求入参
d = eval(p)
print(d)
# json.loads()
# d = eval(params)  # 根据的python的数据类型来做转换
# print(d['status'])

d1 = json.loads(params)
print(type(d1), d1)
print(d1['msg'])
