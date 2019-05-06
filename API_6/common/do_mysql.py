# -*- coding:utf-8 _*-
"""
@author:mongo
@time: 2018/12/17
@email:3126972006@qq.com
@function：
"""
import pymysql


class DoMysql:
    """
    完成与MySQL数据库的一个交互
    """

    def __init__(self):
        # 把这些参数放到配置文件里面去做，然后在这里读取配置文件
        host = "test.lemonban.com"
        user = "test"
        password = "test"
        port = 3306
        # 创建连接
        self.mysql = pymysql.connect(host=host, user=user, password=password, port=port, charset='utf8')
        self.cursor = self.mysql.cursor()  # 创建游标

    def fetch_one(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchone()  # 返回一条数据，元组

    def fetch_all(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()  # 返回多条数据的时候，元组里面套元组

    def close(self):
        self.cursor.close()  # 关闭游标
        self.mysql.close()  # 关闭连接


if __name__ == '__main__':
    mysql = DoMysql()
    result1 = mysql.fetch_one('select max(mobilephone) from future.member')  # 返回一条数据，元组
    print(type(result1), result1)
    result2 = mysql.fetch_all('select * from future.member limit 10')  # 返回多条数据的时候，元组里面套元组
    print(type(result2), result2)
    mysql.close()
