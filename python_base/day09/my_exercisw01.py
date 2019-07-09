# class Student:
#     pass
#
# s=Student()
# s.name='张三'
# s.sex='男'
# s.age=25
# s.score=55.3
# print(s.__dict__)

# class S:
#
#     def __init__(self,name,sex,age,score):
#         self._name=name
#         self._sex=sex
#         self._age=age
#         self._score=score
#
#     def print_self(self):
#         self._love='打篮球'
#         print(self._name+' '+self._sex+' '
#               +str(self._age)+' '+str(self._score)+' '+self._love)
#
# s01=S('李四','男',33,99)
#
# s01.print_self()
# print(s01.__dict__)

# class Vector:
#     """
#         二维向量类
#     """
#     def __init__(self,x=0,y=0):
#         """
#             实例化向量
#         :param x: 横坐标
#         :param y: 纵坐标
#         """
#         self.x=x
#         self.y=y
#     @staticmethod
#     def up():
#         """
#             向上操作
#         :return:
#         """
#         return Vector(-1,0)
#
#     @staticmethod
#     def down():
#         """
#             向下操作
#         :return:
#         """
#         return Vector(1,0)
#
#     @staticmethod
#     def left():
#         """
#             向左操作
#         :return:
#         """
#         return Vector(0,-1)
#
#     @staticmethod
#     def right():
#         """
#             向右操作
#         :return:
#         """
#         return Vector(0,1)
#
# target_list=[
#     ['00','01','02','03'],
#     ['10','11','12','13'],
#     ['20','21','22','23'],
#     ['30','31','32','33']
#
# ]
#
# def get_element(listing,pos,vec,_len):
#     temp=[]
#     for i in range(_len):
#         pos.x+=vec.x
#         pos.y+=vec.y
#         temp.append(listing[pos.x][pos.y])
#     return temp

# v=Vector(2,3)
#
# re=get_element(target_list,v,Vector.left(),2)
#
# print(re)

class A:

    total_number=100
    @classmethod
    def print_cls(cls):
        print(cls.total_number)

    def __init__(self,name,number):
        self.name=name
        self.number=number
        A.total_number-=self.number

    # def num1(self,number):
    #     self.number=number
    #     A.total_number-=self.number
    #
    # def num2(self,number):
    #     self.number=number
    #     A.total_number-=self.number

a=A('ZHANGSAN',20)
print(a.total_number)
A.print_cls()
a.print_cls() # 不建议通过对象访问类方法

b=A('lisi',40)
A.print_cls()

print(b.total_number)
# b.print_cls()