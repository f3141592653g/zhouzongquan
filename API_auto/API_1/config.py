# _*_ coding: utf_8 _*_
# @Time     : 2019/3/12
# @Author   : yuandian
# @Email    : 919839065@qq.com
# @file     : class_0312
from configparser import ConfigParser
from API_auto.API_1 import file_name


class ConfigParsers:
    def __init__(self, encoding='utf-8'):
        self.conf = ConfigParser()
        self.encoding = encoding
        self.conf.read(file_name.change_file, encoding)
        self.conf.read(file_name.sheet_file, encoding)
        self.conf.read(file_name.jdbc_file, encoding)
        self.conf.read(file_name.log_conf_file, encoding)

        swich = self.conf.getboolean("swich", "on")
        if swich:
            self.conf.read(file_name.develop_file, encoding)
        else:
            self.conf.read(file_name.test_file, encoding)

    def get(self, section, option):
        return self.conf.get(section, option)


if __name__ == '__main__':
    CP = ConfigParsers()
    cc = CP.get("connect", "port")
    print(cc)
