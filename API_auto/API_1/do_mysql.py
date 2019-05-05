# _*_ coding: utf_8 _*_
# @Time     : 2019/3/12
# @Author   : yuandian
# @Email    : 919839065@qq.com
# @file     : class_0312

import pymysql
from API_auto.API_1.config import ConfigParsers


class DoMysql:
    def __init__(self):
        CP = ConfigParsers()
        host = CP.get("connect", "host")
        user = CP.get("connect", "user")
        password = CP.get("connect", "password")
        port = int(CP.get("connect", "port"))
        self.mysql = pymysql.connect(host=host, user=user, password=password, port=port, charset="utf8")
        self.cursor = self.mysql.cursor()  # 创建游标

    def sel_one(self, sql):
        self.cursor.execute(sql)
        self.mysql.commit()
        return self.cursor.fetchone()

    def sel_all(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def sel_close(self):
        self.cursor.close()
        self.mysql.close()


if __name__ == '__main__':
    DM = DoMysql()
    one = DM.sel_one('select max(mobilephone) from future.member')
