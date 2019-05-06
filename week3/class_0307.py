# _*_ coding: utf_8 _*_



# 1：创建一个名为 Restaurant 的类，其方法 init ()设置两个属性： restaurant_name 和 cooking_type。创建一个名为 describe_restaurant()的方法和一个名为
# open_restaurant()的方法，其中前者打印前述两项信息，而后者打印一条消息， 指出餐馆正在营业。 根据这个类创建一个名为 restaurant 的实例，分别打印其两个属性，再调用前述两个方法。

class Restaurant:
    def __init__(self,restaurant_name,cooking_type):
        self.restaurant_name = restaurant_name
        self.cooking_type = cooking_type

    def describe_restaurant(self):
        print("{}".format(self.restaurant_name))
        print("{}".format(self.cooking_type))

    def open_restaurant(self):
        print("餐馆正在营业")

restaurant = Restaurant("男朋友","女朋友")
print("{}{}".format(restaurant.restaurant_name,restaurant.cooking_type))
restaurant.describe_restaurant()
restaurant.open_restaurant()


# 2:建一个名为 User 的类，其中包含属性 first_name 和 last_name，还有用户简介通常会存储的其他几个属性。在类 User 中定义一个名为 describe_user()的方法，它打印用户信息摘要；再定义一个名为 greet_user()的方法，它向用户发出个性化的问候。

#
class User:
    #属性
    first_name="yuandian"
    last_name="原点"

    def bescribe_user(self,sex,high,hobby):
        print("他的性别是:{},身高是：{}，爱好是：{}".format(sex,high,hobby))

    @staticmethod
    def greet_user():
        print("你好，{}".format(User.first_name))

User().bescribe_user(sex="男",high="170",hobby="玩游戏")
User().greet_user()





# 3：思考问题：
# #3.1为什么会有对象方法 类方法 静态方法？我什么时候写什么类型的方法呢？
# #3.2什么时候用？
# #3.3写成不同的方法类型 有啥用呢？对我来说有啥用?
# #3.4他们有什么区别呢？ #自己总结一波。

"""答：
3.1：为了在调用起来更加合理和方便。  
在需要用到类的实例使用的方法的时候，我们一般使用对象方法           
我们需要将类本身最为一个对象进行调用的时候，我们可以使用类方法
静态方法是类中的函数，不需要实例。可以理解为一个独立的函数。所以当我们的操作不会涉及到类中的属性和方法的时候，我们可以使用静态方法

3.2：同上
3.3：写成不同类型，可以更加合理的调用，使用起来更加方便。别人看我的代码的时候，一眼就能知道这个方法是否会涉及到类的属性以及方法。反正就很方便啦
3.4区别：
1、对象方法：是对类实例化后的对象有效的，只能由对象调用
2、类方法：第一个参数是cls，是对当前类做的额外的处理,类方法是类可以调用，对象也可以调用。装饰器@classmethod
3、静态方法：没有参数。类可以调用，对象也可以调用。装饰器@staticmethod

"""


