# _*_ coding:utf_8 _*_
# @Time     : 2019/3/20 22:56
# @Author   : yuandian
# @Email    : 919839065@qq.com
# @file     : class_0320.py

import logging
from API_auto.API_1.config import ConfigParsers
from API_auto.API_1 import file_name


class Logger:
    def __init__(self, log_collector, encoding="utf-8"):
        self.log_collector = log_collector
        self.encoding = encoding
    def log(self):
        log_lv = ConfigParsers().get("log", "logger_level")
        log_msg = ConfigParsers().get("log", "logger_fmt")
        my_logger = logging.getLogger(self.log_collector)  # 创建一个日志收集器
        my_logger.setLevel(log_lv)

        fmt = logging.Formatter(log_msg)

        channel = logging.StreamHandler()  # 指定输出到控制台
        channel.setLevel(log_lv)
        channel.setFormatter(fmt)  # 格式化输出

        file_log = logging.FileHandler(file_name.log_file + '/py15.log')  # 指定输出到py15.log日志文件
        file_log.setLevel(log_lv)
        file_log.setFormatter(fmt)

        my_logger.addHandler(channel)
        my_logger.addHandler(file_log)

        file_log.close()
        return my_logger

#     def remove_log(self):
#         self.my_logger.removeHandler(self.file_log)
#         self.my_logger.removeHandler(self.channel)
#
#
# logger = Logger("py15").log()
#
# logger.info("测试一下")
# logger = Logger("py15").remove_log()