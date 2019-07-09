"""
    练习
    1.创建一个数据表为user
    2.编写程序完成如下功能
    * 注册，终端输入 用户名和密码，将用户名和密码存入数据库
    用户名不能重复
    * 登录，终端输入用户名和密码，如果该用户存在则得到登录成功
    不存在则登录失败
    3.将数据库操作功能封装为类
"""
# import pymysql

from login import Login
user=Login()

def do_login():
    user_name = input("User name:")
    passwd = int(input("PassWD:"))
    return user.login(user_name,passwd)

def do_register():
    user_name = input("User name:")
    passwd = int(input("PassWD:"))
    return user.register(user_name,passwd)

while True:
    print("===========================")
    print("**          login        **")
    print("**        register       **")
    print("===========================")
    cmd=input("Cmd:")
    if cmd == 'login':
        if do_login():
            print("登录成功")
        else:
            print("登录失败")
        continue
    elif cmd == 'register':
        if do_register():
            print("注册成功")
        else:
            print("注册失败")
        continue
    elif not cmd:
        print("退出界面")
        break
    else:
        print("重新输入")
user.myclose()
# # 创建连接
# db = pymysql.connect(
#     host='localhost',
#     port=3306,
#     user='root',
#     passwd='123456',
#     database='User',
#     charset='utf8'
# )
#
# # 创建游标
# cur= db.cursor()
#
# user_name=input("User name:")
# passwd=int(input("PassWD:"))
#
#
# sql="select * from user where user_name = %s;"
#
# try:
#     cur.execute(sql,[user_name])
#     data=cur.fetchone()
#
# except Exception as e:
#     db.rollback()
# else:
#     if not data:
#         print("该用户不存在")
#         print("登录失败")
#     elif data[2] == passwd:
#         print("登录成功")
#     else:
#         print("密码错误")
#         print("登录失败")