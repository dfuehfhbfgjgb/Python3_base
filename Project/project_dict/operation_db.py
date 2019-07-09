"""
    dict项目用于处理数据
"""
import pymysql
import hashlib
import time
class Database:

    def __init__(
            self,
            host='localhost',
            port=3306,
            user='root',
            passwd='123456',
            database='DICT',
            charset='utf8'
    ):

      self.host=host
      self.port=port
      self.user=user
      self.passwd=passwd
      self.database=database
      self.charset=charset
      self.connect_db() # 链接数据库

    def connect_db(self):
        self.db = pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            passwd=self.passwd,
            database=self.database,
            charset=self.charset
        )


    # 创建游标
    def create_cursor(self):
        self.cur = self.db.cursor()

    # 关闭数据库链接
    def close(self):
        self.cur.close()
        self.db.close()

    # 处理注册
    def register(self,name,passwd):
        sql="select * from user where name = '%s';"%name
        self.cur.execute(sql)
        r=self.cur.fetchone()
        # 如果查找到结果注册失败
        if r:
            return False
        sql="insert into user (name,passwd) values (%s,%s);"
        hash = hashlib.md5((name + "the-salt").encode())
        hash.update(passwd.encode())
        try:
            self.cur.execute(sql,[name,hash.hexdigest()])
            self.db.commit()
            return True
        except Exception:
            self.db.rollback()
            return False

    def login(self,name,passwd):
        sql="select * from user where name = %s and passwd = %s"
        hash = hashlib.md5((name + "the-salt").encode())
        hash.update(passwd.encode())
        self.cur.execute(sql,[name,hash.hexdigest()])
        r=self.cur.fetchone()
        # 如果查到结果登录成功
        if r:
            return True
        else:
            return False

    # 插入历史记录
    def insert_history(self,name,word):
        tm=time.ctime()
        sql="insert into hist (name,word,time) values (%s,%s,%s);"
        try:
            self.cur.execute(sql,[name,word,tm])
            self.db.commit()
        except Exception:
            self.db.rollback()

    # 查单词
    def query(self,word):
        sql="select mean from words where word = '%s'"%word

        self.cur.execute(sql)

        r=self.cur.fetchone()
        if r:
            return r[0]

    # 查历史记录
    def query_history(self,name):
        sql="select name,word,time from hist where name = '%s' order by id DESC limit 10;"%name
        self.cur.execute(sql)
        return self.cur.fetchall()
        # print(self.cur.fetchall())
    # 修改密码
    def alter_passwd(self,name,old_passwd,new_passwd):
        sql = "select * from user where name = %s and passwd = %s"
        hash = hashlib.md5((name + "the-salt").encode())
        hash.update(old_passwd.encode())
        temp=hash.hexdigest()
        self.cur.execute(sql, [name,temp])
        # r = self.cur.fetchone()
        if self.cur.fetchall():
            sql = "update user set passwd = %s where name = %s and passwd = %s;"
            hash = hashlib.md5((name + "the-salt").encode())
            hash.update(new_passwd.encode())
            try:
                self.cur.execute(sql, [hash.hexdigest(),name, temp])
                self.db.commit()
                return True
            except Exception:
                self.db.rollback()
                return False
        else:
            return False
if __name__=="__main__":
    db=Database()
    db.create_cursor()
    db.query_history('levi')