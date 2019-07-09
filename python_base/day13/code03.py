"""
    模块属性
    # 练习: 将学生管理系统拆分为四个模块
    # XXXModel  ---> model 模型层
    # XXXView --->  ui  表示层
    # XXXController ---> bll   业务逻辑层
    # 调用代码  --->  main  程序入口
"""
from module01 import *

fun01()
fun03()

# 获取模块文档注释
import my_exercise01 as me
# import text
print(me.__doc__)

# 获取模块文件路径
print(me.__file__)

# 获取模块名称
print(me.__name__) #模块名  __main__


















