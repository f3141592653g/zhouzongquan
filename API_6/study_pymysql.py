# -*- coding:utf-8 _*-
""" 
@author:mongo
@time: 2018/12/17 
@email:3126972006@qq.com
@function： 
"""

import pymysql

# 1,建立连接：数据库的连接信息：
host = "test.lemonban.com"
user = "test"
password = "test"
port = 3306
mysql = pymysql.connect(host=host, user=user, password=password, port=3306)
# 2,新建一个查询页面
cursor = mysql.cursor()
# 3， 编写SQL
sql = 'select max(mobilephone) from future.member'
# sql = 'select * from future.loan limit 10'
# 4，执行SQL
cursor.execute(sql)
# 5，查看结果
result = cursor.fetchone()  # 获取查询结果集里面最近的一条数据返回
# results = cursor.fetchall()  # 获取全部结果集
print(type(result), result[0])
# 6，关闭查询
cursor.close()
# 7，关闭数据库连接
mysql.close()
