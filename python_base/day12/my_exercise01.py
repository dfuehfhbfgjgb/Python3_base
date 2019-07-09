# class Parent:
#     def __init__(self,money):
#         self.total_money=money
#
# class Son(Parent):
#     def __init__(self,money,name):
#         super().__init__(money)
#         self.name=name
#
#     def lay_out(self,money):
#         self.total_money-=money
#         return self.total_money
#
# p=Parent(100000)
#
# s01=Son(10000,'大儿子')
# re=s01.lay_out(1000)
# print(re)

# class EnployeeManage:
#     def __init__(self,name,job):
#         self.name=name
#         self.job=job
#
#     def get_salary(self):
#
#         return self.job.count_salary()
#
# class Job:
#     def __init__(self,base_salary):
#         self.base_salary=base_salary
#
#     def count_salary(self):
#         return self.base_salary
#
# class Programmer(Job):
#     def __init__(self,base_salary,bonus):
#         super().__init__(base_salary)
#         self.bonus=bonus
#
#     def count_salary(self):
#         return self.base_salary+self.bonus
#
# re01=EnployeeManage('老王',Programmer(9000,5000)).get_salary()
# print(re01)

class Student:
    def __init__(self,name,sex,age,score):
        self.name=name
        self.sex=sex
        self.age=age
        self.score=score
    #
    def __str__(self):

        return self.name+' '+self.sex+' '+\
               str(self.age)+' '+str(self.score)

    def __repr__(self):
        return 'Student("%s","%s",%d,%.2f)'\
               %(self.name,self.sex,self.age,self.score)
s01=Student('老王','男',28,99)
print(s01)
s02=eval(s01.__repr__())
print(s02)