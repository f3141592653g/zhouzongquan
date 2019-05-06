# _*_ coding: utf_8 _*_
# @Time     : 2019/3/12
# @Author   : yuandian
# @Email    : 919839065@qq.com
# @file     : class_0312


# 1：把字符串 元组 列表 字典的数据类型特征画一个思维导图，并提交作业
#
# 2：观察这个数据，输出到控制台，说出你发现的问题并且给出合理的解释
#
# d={"name":'华华', 'hobby':'学Python', 'age':18, 'score':{'en':120,'math':99.99,'ch':'A'}, 'friend':['bay max','小CC','如意'], True:'good_man', 0.02:'python', False:'这个value对应的key是布尔值', (1,2,3):'我就是元组大大！！！', 0:'这是真爱呀', 1:'socre is 99.9'}
#
# 3：拓展：利用input函数（自行去拓展该函数的用法），获取一个日期，日期格式如下所示：20190216，然后针对输入的这个日期，进行一些处理后，输出：2019年2月16日   这个字符串到控制台

d={"name":'华华',
   'hobby':'学Python',
   'age':18,
   'score':{'en':120,'math':99.99,'ch':'A'},
   'friend':['bay max','小CC','如意'],
   True:'good_man',
   0.02:'python',
   False:'这个value对应的key是布尔值',
   (1,2,3):'我就是元组大大！！！',
   0:'这是真爱呀',
   1:'socre is 99.9'}

print(d)

date = input("请输入一个日期：")
if date.isdigit():
    if len(date) == 8:
        print("{}年{}月{}日".format(date[:4],date[4:6],date[6:9]))
    else:
        print("您输入的日期格式不对")
else:
    print("你的输入有误")