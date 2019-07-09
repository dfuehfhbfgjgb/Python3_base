"""
    day08(面向对象)
    1. 面向过程：分析解决问题的步骤，然后逐步实现．
    2. 面向对象：找出解决问题的人，然后分配职责．
    3. 类：创建对象的模板，抽象的概念．
    4.　对象： 具体，存储的是数据．
        从设计角度讲：先有对象，再创建类．
        从编码角度讲：先有类，再创建对象．
    5. 类与类区别：行为不同.
        对象与对象区别：数据不同．
    6. 内存图：
"""

class A:
    def __init__(self,a = 0):
        self.a = a

    def print_self(self):
        print(self.a)

# 创建对象　调用__init__方法
a01 = A(100)
# 通过对象地址，调用方法
a01.print_self()

list01 = [A(5).__repr__(),A(10).__repr__()]
print(list01)
# print([list01[0].__str__,list01[1].__str__])






