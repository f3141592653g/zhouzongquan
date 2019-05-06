# _*_coding=utf-8_*_
#!usr/bin/env python
# @Author:double
import logging
# '''收集：5条
#  输出：3条'''
# # logging.debug("debug级别的信息")
# # logging.info("info级别的信息")
# # logging.warning("warning级别的信息")
# # logging.error("error级别的信息")
# # logging.critical("critical级别的信息")
# #新建一个名字为double的日志收集器
# my_log=logging.getLogger("double")
# print(my_log)
# my_log.setLevel("DEBUG")#设置收集的信息级别，与输出取交集
#
# #指定输出渠道
# my_path=logging.StreamHandler()#指定输出到控制台
# # my_path=logging.FileHandler("hh.txt")#指定输出到控制台
# my_path.setLevel("INFO")#设置输出的信息级别
#
# #设置输出式
# formatter=logging.Formatter("[%(asctime)s]-[%(filename)s]-[%(levelname)s]-[日志信息]：%(message)s")
# my_path.setFormatter(formatter)
#
# #收my_log.debug("debug级别的信息")
# my_log.addHandler(my_path)
# my_log.info("info级别的信息")
# my_log.warning("warning级别的信息")
# my_log.error("error级别的信息")
# my_log.critical("critical级别的信息")
from test.conf import Config
class Log:
    def __init__(self,collect_name,level):
        self.my_log = logging.getLogger(collect_name)
        self.my_log.setLevel(level)
    def log_console(self,config_name):
        my_path=logging.StreamHandler()
        conf = Config(config_name)
        level = conf.get_value("LOG", "output_level")
        my_path.setLevel(level)
        # "[%(asctime)s]-[%(filename)s]-[%(levelname)s]-[日志信息]：%(message)s"
        form = conf.get_value("LOG", "formatter")
        print(form)
        # formatter = logging.Formatter(form)
        # my_path.setFormatter(formatter)
        # self.my_log.addHandler(my_path)
        # self.my_log.debug("debug信息")
        # self.my_log.info("info信息")
        # self.my_log.warning("warning信息")
        # self.my_log.error("error信息")
        # self.my_log.critical("critical信息")
if __name__ == '__main__':
        log = Log("double", "DEBUG")
        log.log_console("config.cfg")
    # def log_file(self,file_name,config_name):
    #     my_path = logging.FileHandler(file_name)
    #     conf=Config(config_name)
    #     level=conf.get_value("LOG","output_level")
    #     my_path.setLevel(level)
    #     # form=conf.get_value("LOG","formatter")
    #     formatter = logging.Formatter("[%(asctime)s]-[%(filename)s]-[%(levelname)s]-[日志信息]：%(message)s")
    #     my_path.setFormatter(formatter)
    #     self.my_log.addHandler(my_path)
    #     self.my_log.debug("debug信息")
    #     self.my_log.info("info信息")
    #     self.my_log.warning("warning信息")
    #     self.my_log.error("error信息")
    #     self.my_log.critical("critical信息")

    # def log_console(self,level):
    #     my_path=logging.StreamHandler()
    #     my_path.setLevel(level)
    #     formatter = logging.Formatter('[%(asctime)s]-[%(filename)s]-[%(levelname)s]-[日志信息]：%5(message)s')
    #     my_path.setFormatter(formatter)
    #     self.my_log.addHandler(my_path)
    #     self.my_log.debug("debug信息")
    #     self.my_log.info("info信息")
    #     self.my_log.warning("warning信息")
    #     self.my_log.error("error信息")
    #     self.my_log.critical("critical信息")
    # def log_file(self,file_name,config_name):
    #     my_path = logging.FileHandler(file_name)
    #     conf=Config(config_name)
    #     level=conf.get_value("LOG","output_level")
    #     my_path.setLevel(level)
    #     form=conf.get_value("LOG","formatter")
    #     formatter = logging.Formatter(form)
    #     my_path.setFormatter(formatter)
    #     self.my_log.addHandler(my_path)
    #     self.my_log.debug("debug信息")
    #     self.my_log.info("info信息")
    #     self.my_log.warning("warning信息")
    #     self.my_log.error("error信息")
    #     self.my_log.critical("critical信息")



