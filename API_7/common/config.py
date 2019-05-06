# -*- coding:utf-8 _*-
""" 
@author:mongo
@time: 2018/12/17 
@email:3126972006@qq.com
@function： 
"""
import configparser

from API_7.common import contants


class ReadConfig:
    """
    完成配置文件的读取
    """

    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read(contants.global_file)  # 先加载global
        switch = self.config.getboolean('switch', 'on')
        if switch:  # 开关打开的时候，使用online的配置
            self.config.read(contants.online_file, encoding='utf-8')
        else:  # 开关关闭的时候，使用test的配置
            self.config.read(contants.test_file, encoding='utf-8')

    def get(self, section, option):
        return self.config.get(section, option)


config = ReadConfig()

# if __name__ == '__main__':
#     config = ReadConfig()
#     print(config.get('api', 'pre_url'))
