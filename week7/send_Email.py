# _*_ coding: utf_8 _*_
# @Time     : 2019/3/12
# @Author   : yuandian
# @Email    : 919839065@qq.com
# @file     : class_0312
# 1. 自己解决邮件服务商 smtp 协议的配置；
#
# 2. 类包含一个主要使用函数 sendmail, 可以完成带附件的邮件发送。
import smtplib

#选择邮件服务商
with smtplib.SMTP_SSL("smtp.qq.com",465) as server:

    #登录
    server.login("919839065@qq.com","ceocabdvoyapbeae")

    msg = """\\
    From:yuandian
    Subject:test
    你好，原点"""


    #发送邮件
    server.sendmail('919839065@qq.com','919839065@qq.com',msg=msg.encode(encoding="utf-8"))
    server.quit()




