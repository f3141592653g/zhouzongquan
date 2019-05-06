#2：观察这个数据，输出到控制台，说出你发现的问题并且给出合理的解释

#d={"name":'华华', 'hobby':'学Python', 'age':18, 'score':{'en':120,'math':99.99,'ch':'A'}, 'friend':['bay max','小CC','如意'], True:'good_man', 0.02:'python', False:'这个value对应的key是布尔值', (1,2,3):'我就是元组大大！！！', 0:'这是真爱呀', 1:'socre is 99.9'}
#d={"name":'华华',
#    'hobby':'学Python',
#    'age':18,
#    'score':{'en':120,'math':99.99,'ch':'A'},
#    'friend':['bay max','小CC','如意'],
#    True:'good_man',
#    0.02:'python',
#    False:'这个value对应的key是布尔值',
#    (1,2,3):'我就是元组大大！！！',
#    0:'这是真爱呀',
#    1:'socre is 99.9'}
#
# print(d)

#### 发现：   true 对应的value值被1对应的value值覆盖了。   false对应的value值被0对应的value值覆盖了。   key 0和1 没有了

#3：拓展：利用input函数（自行去拓展该函数的用法），获取一个日期，日期格式如下所示：20190216，然后针对输入的这个日期，进行一些处理后，输出：2019年2月16日   这个字符串到控制台
# time=input('请输入时间：')
# print("{}年{}月{}日".format(time[:4],time[4:6],time[-2:]))

# score=int(input("请输入数字"))
# if score>90:
#     print("great")
# else :
#     print("no")



