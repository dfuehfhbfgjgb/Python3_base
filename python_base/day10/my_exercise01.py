"""
    __slots__ 属性
"""
# class SkillData:
#     # 限制当前类,创建的对象,只能具有的实例变量.
#     # __slots__ = ("__name","__ask","__speed")
#     # pass
#     def __init__(self,name,ask,speed):
#         self.__name = name
#         self.__ask = ask
#         self.__speed = speed
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, value):
#         self.__name = value
#
#     @property
#     def ask(self):
#         return self.__ask
#     @ask.setter
#     def ask(self,value):
#         self.__ask=value
#
#     @property
#     def speed(self):
#         return self.__speed
#     @speed.setter
#     def speed(self,value):
#         self.__speed=value
#
#
# s01 = SkillData('降龙十八掌',50,10)
# # s01.__name='降龙十八掌'
# s01.ask=100
# # s01.speed=10
# # s01.name = "降龙十八掌"
# # s01.ask=50
# # print(s01.name)
# # 为当前对象,添加实例变量
# # s01.time = 5
# # print(s01.time)
# print(s01.__dict__) # 因为使用了__slots__属性,所以不是使用__dict__.
#
# print(s01.ask)

# 老张开车去东北
# 人类与交通工具类

# class Person:
#     """
#         人类
#     """
#     def __init__(self,name):
#         self.name=name
#
#     def go_to(self,way,place):
#         print(self.name+way.run(place))
#
# class Car:
#     def run(self,place):
#         return '开车去'+place
#
# p=Person('老王')
# c=Car()
# p.go_to(c,'东北')

class G:
    def __init__(self,a):
        # 写入操作
        self.a = a

    def set_a(self, value):
        print("设置变量喽")
        self.__a = value

    # 拦截对变量a的写入操作
    a = property(None,set_a)

g=G(100)
g.a=200
# g.set_a(1)
print(g.__dict__)
# print(g.set_a)