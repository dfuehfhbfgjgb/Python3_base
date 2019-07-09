"""
    dict 服务端部分
    处理请求逻辑
"""
from operation_db import *
from socket import *
from multiprocessing import Process,Pipe
import signal
import time
import sys
# import pymysql

# 全局变量
HOST='0.0.0.0'
PORT=8000
ADDR=(HOST,PORT)
# target_dict={}

# 创建管道
# fd1, fd2 = Pipe(False)  # False:fd1只能读recv（），fd2只能写send（）

# 处理登录
def do_login(c,db,data):
    tmp=data.split(' ')
    name=tmp[1]
    passwd=tmp[2]
    if db.login(name,passwd):
        # 向管道写入内容
        # fd2.send((data,c))
        c.send(b'OK')
    else:
        c.send(b'FAIL')

# 处理注册
def do_register(c,db,data):
    tmp=data.split(' ')
    name = tmp[1]
    passwd=tmp[2]
    if db.register(name,passwd):
        c.send(b'OK')
    else:
        c.send(b'FAIL')

# 处理查询
def do_query(c,db,data):
    tmp = data.split(' ')
    name = tmp[1]
    word = tmp[2]
    db.insert_history(name,word) # 插入历史记录
    mean=db.query(word) #查单词
    if not mean:
        c.send("没有找到该单词".encode())
    else:
        msg="%s : %s"%(word,mean.lstrip())
        c.send(msg.encode())
# 处理历史查询
def do_history(c,db,data):
    tmp=data.split()
    name=tmp[1]
    r=db.query_history(name)
    if not r:
        c.send("没有历史记录".encode())
        return
    c.send(b'OK')
    for i in r:
        msg = "%s       %s      %s"%i
        time.sleep(0.1)
        c.send(msg.encode())
    time.sleep(0.1)
    c.send(b"##")

#修改密码
def alter_passwd(c,db,data):
    tmp=data.split()
    name=tmp[1]
    old_passwd=tmp[2]
    new_passwd=tmp[3]
    r=db.alter_passwd(name,old_passwd,new_passwd)
    if r:
        c.send(b'OK')
    else:
        c.send(b"Alter passwd fail")

# 处理客户端请求
def do_request(c,db):
    db.create_cursor() # 生成游标 db.sur
    while True:
        data=c.recv(1024).decode()
        if not data or data[0]=='E':
            # db.close()
            c.close()
            sys.exit("客户端退出")

            # print(c.getpeername(),":客户端异常退出")
            # return
        # print(c.getpeername(),":",data)
        if data[0]=='R':
            do_register(c,db,data)
        if data[0]=='L':

            do_login(c,db,data)
        if data[0]=='Q':
            do_query(c,db,data)
        if data[0]=='H':
            do_history(c,db,data)
        if data[0]=='A':
            alter_passwd(c,db,data)
# 网络链接
def main():
    # 创建数据库链接对象
    db=Database()

    # 创建套接字
    sockfd=socket()
    sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    sockfd.bind(ADDR)
    sockfd.listen(5)

    # 处理僵尸进程
    signal.signal(signal.SIGCHLD,signal.SIG_IGN)


    #创建在线客户字典
    user_dict={}
    # 创建存储进程仓库
    p_dict={}

    # 等待客户连接
    while True:
        try:
            c,addr=sockfd.accept()
            print("Connect from",addr)
        except KeyboardInterrupt:
            sockfd.close()
            # db.close()
            sys.exit("退出服务器")
        except Exception as e:
            print(e)
            continue
        p=Process(target=do_request,args=(c,db))

        p_dict[c]=p  # 以客户端套接字为键，子进程为值

        p.daemon=True
        p.start()

if __name__=="__main__":
    main()
