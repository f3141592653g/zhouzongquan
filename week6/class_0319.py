# _*_ coding: utf_8 _*_
# @Time     : 2019/3/12
# @Author   : yuandian
# @Email    : 919839065@qq.com
# @file     : class_0312
import logging


class Pylog:

    def __init__(self):
        pass

    def log_work(self,log_ger,level):

        log = logging.getLogger(log_ger)#日志收集器
        log.setLevel(level)

        fmt = logging.Formatter('%(asctime)s-%(filename)s-%(levelname)s-日志信息：%(message)s')

        channel = logging.StreamHandler() #输出渠道
        # channel.setLevel("INFO")
        channel.setFormatter(fmt)

        log.addHandler(channel)
        log.debug("debug message")
        log.info("info message")
        log.warning("warning message")
        log.error("error message")
        log.critical("critical message")
if __name__ == '__main__':
    
    pl = Pylog()
    pl.log_work("python","ERROR")