# _*_ coding: utf_8 _*_
# @Time     : 2019/3/12
# @Author   : yuandian
# @Email    : 919839065@qq.com
# @file     : class_0312

import re
from API_auto.API_1 import config
import configparser


class Regular:
    loan_id = None
    memer_id = None
    def context(self, data):
        p = "#(.*?)#"
        while re.search(p, data):
            find_price = re.search(p, data)  # 循环查找
            param_price = find_price.group(1)  # 拿到参数化的key

            try:
                cf = config.ConfigParsers().get('data', param_price)
            except configparser.NoOptionError as e:  # 如果配置文件里面没有的时候，Regular找
                if hasattr(Regular, param_price):
                    cf = getattr(Regular, param_price)
                else:
                    print("找不到参数化的key")
                    raise e
            print(param_price)
            data = re.sub(p, cf, data, count=1)
        return data
