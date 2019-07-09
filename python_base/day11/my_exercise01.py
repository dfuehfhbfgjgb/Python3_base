# class Player:
#     def __init__(self,name,atk,hp):
#         self.name=name
#         self.atk=atk
#         self.hp=hp
#
#     def attack(self,object):
#         print("玩家%s攻击敌人%s"%(self.name,object.name))
#         object.damage(self.atk)
#     def damage(self,value):
#         self.hp-=value
#         if self.hp>0:
#             print("玩家%s受伤了"%self.name)
#         else:
#             self.death()
#     def death(self):
#         print("玩家%s死亡，碎屏"%self.name)
#
# class Enemy:
#     def __init__(self,name,atk,hp):
#         self.name=name
#         self.atk=atk
#         self.hp=hp
#
#     def attack(self,object):
#         print("敌人%s攻击玩家%s"%(self.name,object.name))
#         object.damage(self.atk)
#
#     def damage(self,value):
#         self.hp-=value
#         if self.hp>0:
#             print("敌人%s受伤了"%self.name)
#         else:
#             self.death()
#
#     def death(self):
#         print("敌人%s死亡,播放音乐"%self.name)
#
# p=Player('张三',20,50)
# e=Enemy('李四',10,30)
#
# p.attack(e)
# e.attack(p)
# e.attack(p)
# # p.attack(e)
# e.attack(p)
# e.attack(p)
# e.attack(p)

#练习1:定义父类--宠物, 行为:吃
    #     定义子类--狗, 行为:防守xx
    #     定义子类--鸟, 行为:飞
    #创建相应对象,调用相应方法.测试isinstance,issubclass函数

# class Pet:
#     def action(self):
#         print("吃")
#
# class Dog(Pet):
#
#     def dog_action(self):
#         print("看家")
#
# class Bird(Pet):
#     def bird_action(self):
#         print("飞翔")
#
# p=Pet()
#
# d=Dog()
# d.action()
# d.dog_action()
# print("================")
#
# b=Bird()
# b.action()
# b.bird_action()
#
# print(isinstance(b,Bird))
# print(issubclass(Dog,Pet))

class Person:
    def __init__(self,name):
        self.name=name

    def go_to(self,vehicle,place):
        print(self.name)
        vehicle.run(place)

class Vehicle:
    def run(self,place):
        raise NotImplementedError("儿子没有这个方法")

class Car(Vehicle):
    def run(self,place):
        print("开车去%s"%place)

class Train(Vehicle):
    def run(self,place):
        print("乘车去%s"%place)

class Plane(Vehicle):
    def run(self,place):
        print("坐飞机去%s"%place)
p01=Person('老王')
p02=Person('老张')
c=Car()
t=Train()
p=Plane()
p02.go_to(c,'东北')