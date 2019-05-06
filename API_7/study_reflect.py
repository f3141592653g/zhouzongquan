# -*- coding:utf-8 _*-
""" 
@author:mongo
@time: 2018/12/17 
@email:3126972006@qq.com
@function： 
"""


class People:
    number_eye = 2

    def __init__(self, name, age):
        self.name = name
        self.age = age


if __name__ == '__main__':
    p = People('mongo', 18)
    print(People.number_eye)
    print(p.number_eye)
    print(p.name)

    # 添加属性
    print(hasattr(People, "number_leg"))  # 如果有返回True, 没有返回FALSE
    print(hasattr(People, "number_eye"))

    setattr(People, "number_leg", 2)
    print(hasattr(People, "number_leg"))
    print(People.number_leg)
    setattr(p, "name", "huahua")
    print(getattr(p, "name"))  # 获取实例属性

    setattr(p, "dance", True)
    print(p.dance)

    getattr(People, "number_leg")  # 获取类属性
    getattr(p, "dance")  # 获取实例属性

    delattr(p, "dance")  # 删除
    getattr(p, "dance")  # 获取实例属性
