# -*- coding:utf-8 _*-
""" 
@author:mongo
@time: 2018/12/17 
@email:3126972006@qq.com
@function： 
"""
import configparser
import re

from API_7.common.config import config


class Context:
    loan_id = None


def replace(data):
    p = "#(.*?)#"  # 正则表达式
    while re.search(p, data):
        print(data)
        m = re.search(p, data)  # 从任意位置开始找，找第一个就返回Match object, 如果没有找None
        g = m.group(1)  # 拿到参数化的KEY
        try:
            v = config.get('data', g)  # 根据KEY取配置文件里面的值
        except configparser.NoOptionError as e:  # 如果配置文件里面没有的时候，去Context里面取
            if hasattr(Context, g):
                v = getattr(Context, g)
            else:
                print('找不到参数化的值')
                raise e
        print(v)
        # 记得替换后的内容，继续用data接收
        data = re.sub(p, v, data, count=1)  # 查找替换,count查找替换的次数

    return data
