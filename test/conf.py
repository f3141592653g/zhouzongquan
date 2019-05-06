# _*_coding=utf-8_*_
#!usr/bin/env python
# @Author:double
# 3-16 定义一个配置类，实现配置文件的数据读取。
# 如题。利用configParser类来实现自己的功能封装。
# 可参考课堂上的类定义。也可以再扩展
# from configparser import ConfigParser
# cf=ConfigParser()
# cf.read("conf.cfg",encoding="utf-8")#文件读取
# sec=cf.sections()  #读取所有的section，列表方式存储
# print(sec)
#
# # print(cf.options(sec[0]))#读取某一section下的所有option,列表方式存储
# # print(cf.options("db"))
# # print(cf.get(sec[0],"db_password"))#获取某一section下的某一option的value，以字符串方式存储
# # print(cf.get("db","db_password"))
# # print(eval(cf.get(sec[0],"db_dic")))#获取本来的数据类型的option
# # print(cf.get(sec[0],"db_list"))
# print(cf.getint(sec[0],"db_password"))#以int方式获取
# print(cf.getfloat(sec[0],"db_password"))#以float方式获取
# print(cf.getboolean(sec[0],"db_yn"))#以boolean方式获取


# 前提：打开配置文件---初始化
# 读取想要的数据：section option value（各种类型数据）
import configparser
class Config:
    def __init__(self,conf_filename_path,encoding="utf-8"):
        self.cf=configparser.RawConfigParser()
        self.cf.read(conf_filename_path,encoding)

    def get_section(self):
        return self.cf.sections()

    def get_options(self,sec):
        return self.cf.options(sec)

    def get_value(self,sec,res):
        # S=self.cf.sections()
        # op=self.cf.options(S[sec])
        # os=self.cf.get(S[sec],res)
        # print(op, os)
       return self.cf.get(sec,res)

    def get_int_value(self,sec,res):
        # S = self.cf.sections()
        # op = self.cf.options(S[sec])
        # os = self.cf.getint(S[sec], res)
        # print(op, os)
        return self.cf.getint(sec, res)

    def get_float_value(self,sec,res):
        # S = self.cf.sections()
        # op = self.cf.options(S[sec])
        # os = self.cf.getfloat(S[sec], res)
        # print(op, os)
        return self.cf.getfloat(sec, res)

    def get_boolean_value(self,sec,res):
        # S = self.cf.sections()
        # op = self.cf.options(S[sec])
        # os = self.cf.getboolean(S[sec], res)
        # print(op, os)
        return self.cf.getboolean(sec, res)

    def get_real_value(self,sec,res):
        # S = self.cf.sections()
        # op = self.cf.options(S[sec])
        # os = eval(self.cf.getint(S[sec], res))
        # print(op, os)
        return eval(self.cf.get(sec, res))


if __name__ == '__main__':
    t=Config("conf.cfg")
    x=t.get_value("db","db_name")
    y=t.get_section()
    z=t.get_options("db")
    print(x)
    print(y)
    print(z)

    # t.get_boolean_value(0,"db_yn")







