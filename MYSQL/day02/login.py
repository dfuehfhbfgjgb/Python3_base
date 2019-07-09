import pymysql

class Login:

    def __init__(self,
                 database='User',
                 host='localhost',
                 user='root',
                 passwd='123456',
                 port=3306,
                 charset='utf8',
                 table='login'):

        self.database=database
        self.host=host
        self.user=user
        self.passwd=passwd
        self.port=port
        self.charset=charset
        self.table=table
        self.connect_db() # 连接数据库

    def connect_db(self):
        self.db=pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            passwd=self.passwd,
            database=self.database,
            charset=self.charset
        )
        self.cur=self.db.cursor()
    def myclose(self):
        self.cur.close()
        self.db.close()

    # 登录
    def login(self,user_name,passwd):
        sql = "select * from %s where user_name = '%s' and \
               passwd = %d;"%(self.table,user_name,passwd)
        self.cur.execute(sql)
        if self.cur.fetchone():
            return True
        else:
            return False

    # 注册
    def register(self,user_name,passwd):
        sql="select * from %s where user_name = '%s';"%(self.table,user_name)
        self.cur.execute(sql)
        if self.cur.fetchone():
            return False
        sql="insert into %s (user_name,passwd) values ('%s',%d);"%(self.table,user_name,passwd)

        try:
            self.cur.execute(sql)
            self.db.commit()
        except Exception as e:
            print(e)
            self.db.rollback()
            return False
        return True



# if __name__=='__main__':
#     user_name=input("User name:")
#     passwd=int(input("PassWD:"))