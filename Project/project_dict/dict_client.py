"""
     dict 客户端
     发起请求，展示结果
"""
from socket import *
from multiprocessing import Process,Pipe
from threading import Thread
from getpass import getpass
# import os
import signal

#全局变量
s=socket()
ADDR=('176.140.6.128',8000)

# 创建管道
# fd1,fd2=Pipe(False) # False:fd1只能读recv（），fd2只能写send（）

# 查询历史记录
def do_history(name):
    msg="H %s"%name
    s.send(msg.encode())
    data=s.recv(128).decode()
    if data=='OK':
        while True:

            if data=='##':
                break
            data = s.recv(128).decode()
            print(data)
    else:
        print(data)
    # for item in data:
    #     print(item[2],item[3])




# 查单词
def do_query(name):
    while True:
        print("""
        ====输入 ## 退出单词查询====
        """)
        word=input("单词：")
        if word == '##': # 结束单词查询
            break
        msg = "Q %s %s"%(name,word)
        s.send(msg.encode())
        # 等待回复
        data=s.recv(2048).decode()
        # if data == '###':
        #     return "quit"
        print(data)
#修改密码
def alter_passwd(name):
    while True:
        old_passwd=input("Please input your old PassWD:")
        new_passwd=input("Please input your new PassWD:")
        if (' ' in old_passwd) or (' ' in new_passwd):
            print("密码不能有空格")
            continue
        msg="A %s %s %s"%(name,old_passwd,new_passwd)
        s.send(msg.encode())
        data = s.recv(2048).decode()
        if data == 'OK':
            print("修改成功")
            print("请重新登录")
            return
        else:
            print("修改失败")
#三级界面
def do_set(name):
    while True:
        print("""
        ===============set===============
         1.修改密码                 2.返回
        =================================
        """)
        cmd = input(">>>")
        if cmd == '1':
            alter_passwd(name)
            return True
        elif cmd == '2':
            return

# 二级界面
def login(name):

    while True:
        while True:
            print("""
            ==============Query==================
              1.查单词  2.历史记录  3.注销  4.设置
            =====================================
            """)
            cmd = input("输入选项：")
            if cmd == '1':
                do_query(name)

            elif cmd == '2':
                do_history(name)
            elif cmd == '3':
                return
            elif cmd == '4':
                if do_set(name):
                    return

# 注册
def do_register():
    while True:
        name=input("User：")
        # 隐藏输入内容，返回值是输入的字符串
        # passwd=getpass()
        # passwd1 = getpass("Again:")
        passwd=input("Passwd:")
        passwd1=input("Again:")
        if (' ' in name) or (' ' in passwd):
            print("用户名或密码不能有空格")
            continue
        if passwd != passwd1:
            print("两次密码不一致")
            continue
        msg="R %s %s"%(name,passwd)
        #发送请求
        s.send(msg.encode())
        # 接收反馈
        data=s.recv(128).decode()
        if data == 'OK':
            print("注册成功")
            login(name)
        else:
            print("注册失败")
        return

# 登录
def do_login():
    while True:
        name=input("User：")
        # 隐藏输入内容，返回值是输入的字符串
        # passwd=getpass()
        passwd = input("Passwd:")
        msg="L %s %s"%(name,passwd)
        s.send(msg.encode())
        # 等待反馈
        data=s.recv(128).decode()
        if data == 'OK':
            print("登录成功")
            login(name)
        else:
            print("登录失败")
        return


# 退出
def do_exit():
    s.send(b'E')

# 处理僵尸进程
    signal.signal(signal.SIGCHLD,signal.SIG_IGN)


def runing():
    # # 创建网络连接
    # s=fd1.recv()
    s.connect(ADDR)

    # #创建线程处理账号登录唯一性
    # t = Thread(target=detection_login,args=(s,))
    # t.setDaemon(True)  # 主线程退出分支线程也退出
    # t.start()

    while True:
        print("""
        ==============Welcome=============
         1.注册        2.登录       3.退出
        ==================================
        """)
        try:
            cmd=input("输入选项：")
        except KeyboardInterrupt:
            print("退出客户端")
            # s.send(b'E')
            break
        if cmd=='1':
            do_register()
        elif cmd=='2':
            do_login()
        elif cmd=='3':
            do_exit()
            return
    s.close()

def detection_login(s):
    while True:
        try:
            data=s.recv(128).decode()
        except Exception:
            print("服务崩溃")
            s.close()
            break
        if data == 'quit':
            s.close()
        else:
            continue




# def main(s):
# #     # 创建网络连接
# #     s.connect(ADDR)
# #
# #     # while True:
# #     p = Process(target=runings)
# #     fd2.send(s)
# #     p.daemon = True
# #     p.start()
#     while True:
#         try:
#             data=s.recv(2048).decode()
#         except:
#             break
#         if data == 'quit':
#             # p.close()
#             break
#         else:
#             continue

if __name__=="__main__":
    runing()
