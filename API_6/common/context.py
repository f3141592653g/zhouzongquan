# -*- coding:utf-8 _*-
""" 
@author:mongo
@time: 2018/12/17 
@email:3126972006@qq.com
@function： 
"""
import re

from API_6.common.config import config


def replace(data):
    p = "#(.*?)#"  # 正则表达式
    while re.search(p, data):
        print(data)
        m = re.search(p, data)  # 从任意位置开始找，找第一个就返回Match object, 如果没有找None
        g = m.group(1)  # 拿到参数化的KEY
        print(g)
        v = config.get('data', g)  # 根据KEY取配置文件里面的值
        print(v)
        # 记得替换后的内容，继续用data接收
        data = re.sub(p, v, data, count=1)  # 查找替换,count查找替换的次数

    return data


er = replace("normal_user")
print(er)