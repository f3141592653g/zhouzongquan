# _*_ coding:utf_8 _*_
# @Time     : 2019/3/20 22:56
# @Author   : yuandian
# @Email    : 919839065@qq.com
# @file     : class_0320.py

import logging
from week6.class_0317 import lernConfig


class lern_log:

    def __init__(self, log_collector, log_file, conf_file, encoding, section, option_level, option_fmt):
        self.log_collector = log_collector
        self.log_file = log_file
        self.conf_file = conf_file
        self.encoding = encoding
        self.section = section
        self.option_level = option_level
        self.option_fmt = option_fmt

    def log_input(self):

        log_lv = lernConfig(self.conf_file, self.encoding).get_strValue(self.section,self.option_level)
        log_msg = lernConfig(self.conf_file, self.encoding).get_strValue(self.section,self.option_fmt)
        my_logger = logging.getLogger(self.log_collector)  # 创建一个日志收集器
        my_logger.setLevel(log_lv)

        fmt = logging.Formatter(log_msg)

        channel = logging.StreamHandler()  # 指定输出到控制台
        channel.setLevel(log_lv)
        channel.setFormatter(fmt)  # 格式化输出

        file_log = logging.FileHandler(self.log_file,encoding=self.encoding)  # 指定输出到py15.log日志文件
        file_log.setLevel(log_lv)
        file_log.setFormatter(fmt)

        my_logger.addHandler(channel)
        my_logger.addHandler(file_log)

        my_logger.debug("debug message")
        my_logger.info("info message")
        my_logger.warning("warning message")
        my_logger.error("error message")
        my_logger.critical("critical message")


if __name__ == '__main__':
    lr = lern_log("python15","py15.log","demo.cfg","utf-8","log","logger_level","logger_fmt")
    lr.log_input()
