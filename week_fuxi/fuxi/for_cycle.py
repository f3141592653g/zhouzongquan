# _*_ coding: utf_8 _*_
# @Time     : 2019/3/12
# @Author   : yuandian
# @Email    : 919839065@qq.com
# @file     : class_0312

# 1：人和机器进行猜拳游戏写一段程序，首先选择角色：1 曹操 2张飞 3 刘备，然后选择的角色进行猜拳：1剪刀 2石头 3布 玩家输入一个1-3的数字
# ；然后电脑出拳 随机产生1个1-3的数字，提示电脑出拳结果（ 1剪刀 2石头 3布 ） ，双方出拳完毕后：角色和机器出拳对战，
# 对战结束后，最后出示本局对战结果...赢...输,然后提示用户是否继续？按y继续，按n退出。最后结束的时候输出结果 角色赢几局 电脑赢几局，平局几次 游戏结束


import random


class guess_box:
    def choiceUser(self):
        # 选择角色
        while True:
            user = {1:"曹操", 2:"张飞", 3:"刘备"}
            try:
                role = int(input("请输入数字表示你要选择的角色（1 曹操 2张飞 3 刘备）："))
                if role in user:
                    print("你选择的角色是",user[role])
                    break
                else:
                    print("输入错误，请重新输入")
                    continue
            except Exception as e:
                print("输入错误，请输入数字")
                continue

    def choiceBox(self):
        # 选择的角色进行猜拳
        while True:
            box = {1:"剪刀",2:"石头",3:"布"}
            try:
                guess = int(input("请输入数字表示你要选择的角色（1剪刀 2石头 3布）："))
                if guess in box:
                    print("你出的拳是",box[guess])
                    break
                else:
                    print("输入错误，请重新输入")
                    continue
            except Exception as e:
                print("输入错误，请输入数字")
                continue
        return box[guess]

    def choiceComputer(self):
        box = {1: "剪刀", 2: "石头", 3: "布"}
        # 电脑出拳
        rd = random.randint(1,3)
        print("电脑的出拳是",box[rd])
        return rd

    def last(self):
        if self.choiceBox() == 1:
            if self.choiceComputer() == 1:
                print("平局")
            elif self.choiceComputer() == 2:
                print("机器赢了")
            else:
                print("你赢了")
        elif self.choiceBox() == 2:
            if self.choiceComputer() == 1:
                print("你赢了")
            elif self.choiceComputer() == 2:
                print("平局")
            else:
                print("机器赢了")
        elif self.choiceBox() == 3:
            if self.choiceComputer() == 1:
                print("电脑赢了")
            elif self.choiceComputer() == 2:
                print("你赢了")
            else:
                print("平局")


if __name__ == '__main__':
    guess_box().choiceUser()
    guess_box().choiceBox()
    guess_box().choiceComputer()
    guess_box().last()

# 2：完成1-10的整数数字相加，并打印最后的结果
#
#
# 3.一个足球队在寻找年龄在10岁到12岁的小女孩（包括10岁和12岁）加入。编写一个程序，询问用户的性别（m表示男性，f表示女性）和年龄，然后显示一条消息指出这个人是否可以加入球队，询问10次后，输出满足条件的总人数。
#
#
# 4:利用Python代码画出直角三角形以及等边三角形，如下所示：
#
#
# 5：输出99乘法表
#
#
# 6：经典冒泡算法： 利用for循环，完成a=[1,7,4,89,34,2]的冒泡排序： 冒泡排序：小的排前面，大的排后面。
#
#
# 7：有1 2 3 4 这四个数字，能组成多少个互不相同且无重复数字的三位数？分别是什么？abc a!=b!=c


