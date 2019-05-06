# -*- coding:utf-8 _*-
""" 
@author:mongo
@time: 2018/12/17 
@email:3126972006@qq.com
@function：  解析正则表达式 -->查找
"""
import re

from API_8.common.config import config

data = '{"mobilephone":"#normal_user#","pwd":"#normal_pwd#"}'
# 原本字符,元字符
p = "#(.*?)#"  # 正则表达式
# ms = re.findall(p, data)  # 查找全部，返回列表
# print(ms)
# m = re.search(p, data)  # 从任意位置开始找，找第一个就返回Match object, 如果没有找None
# print(m.group(0))  # 返回表达式和组里面的内容
# print(m.group(1))  # 只返回指定组的内容
# g = m.group(1)  # 拿到参数化的KEY
# v = config.get('data', g)  # 根据KEY取配置文件里面的值
# print(v)
# data_new = re.sub(p, v, data, count=1)  # 查找替换,count查找替换的次数
# print(data_new)

# 如果要匹配多次，替换多次，使用循环来解决

while re.search(p, data):
    print(data)
    m = re.search(p, data)  # 从任意位置开始找，找第一个就返回Match object, 如果没有找None
    g = m.group(1)  # 拿到参数化的KEY
    v = config.get('data', g)  # 根据KEY取配置文件里面的值
    print(v)
    # 记得替换后的内容，继续用data接收
    data = re.sub(p, v, data, count=1)  # 查找替换,count查找替换的次数

print('最后替换后的data', data)