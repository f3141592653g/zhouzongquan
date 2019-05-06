# _*_ coding: utf_8 _*_
# @Time     : 2019/3/12
# @Author   : yuandian
# @Email    : 919839065@qq.com
# @file     : class_0312

# 1.根据你输入的数据，来进行判断学生的成绩。输入数据函数：input()
# try:
#     score = int(input("请输入你的成绩："))
#     if len(str(score)) <= 3:
#         if 80<= score <= 100:
#             print('优秀')
#         elif 60 <= score < 80 :
#            print("及格")
#         elif score < 60:
#             print("不及格")
#         else:
#             print("你的输入有误")
#     else:
#         print("你输入的数字长度不对")
# except Exception as e:
#     print("输入的格式有误")



# 2、一家商场在降价促销。如果购买金额50-100元(包含50元和100元)之间，会给10%的折扣，如果购买金额大于100元会给20%折扣。编写一程序，询问购买价格，再显示出折扣（%10或20%）和最终价格
while 1:
    try:
        price = int(input("请输入价格"))
        if 50<= price <= 100:
            print("{}".format(price*(1-0.1)))
            break
        elif price> 100:
            print("{}".format(price*(1-0.2)))
            break
        else:
            print("输入有误，请重新输入")
            continue
    except Exception as e:
        print("您输入的价格格式不正确，请重新输入")
        continue


# 3、输入一个数，判断一个数n能同时被3和5整除
#
#
#
# 4、输入一个年份，输出是否为闰年，闰年条件：能被4整除但不能被100整除，或者能被400整除的年份都是闰年
#
#
#
# 5、一个 5 位数，判断它是不是回文数。即 12321 是回文数，个位与万位相同，十位与千位相同。 根据判断打印出相关信息。01210
#
#
#
# 6、利用random函数生成随机整数，从1-9取出来。然后输入一个数字，来猜，如果大于，则打印bigger。小了，则打印less。如果相等，则打印equal