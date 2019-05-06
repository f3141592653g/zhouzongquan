# _*_ coding: utf_8 _*_
# @Time     : 2019/3/12
# @Author   : yuandian
# @Email    : 919839065@qq.com
# @file     : class_0312

from configparser import ConfigParser


class Conf():
    def __init__(self,configPath):
        self.cf=ConfigParser()
        self.cf.read(configPath)

    def getVlue(self,section):
        return self.cf.options(section)


if __name__ == '__main__':
    C=Conf("demo.cfg")
    f=C.getVlue("db")
    print(f)
