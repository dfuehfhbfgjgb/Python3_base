import pymysql

# 1. 建立数据库连接(db = pymysql.connect(...))
db = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='123456',
    database='stu',
    charset='utf8'
)

# 2. 创建游标对象(c = db.cursor())
# 获取游标
c = db.cursor()

# 数据操作
# 3. 游标方法: c.execute("insert ....")

# 执行sql语句
c.execute("insert into myclass values (6,'Lily',12,'w',80.0);")

# 4. 提交到数据库 : db.commit()
# 将修改内容提交到数据库
db.commit()

# 5. 关闭游标对象 :c.close()
c.close()
# 6. 断开数据库连接 :db.close()
db.close()