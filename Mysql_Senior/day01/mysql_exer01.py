# db = pymysql.connect(参数列表)
# host :主机地址,本地 localhost
# port :端口号,默认3306
# user :用户名
# password :密码
# database :库
# charset :编码方式,推荐使用 utf8
# 数据库连接对象(db)的方法
# db.close() 关闭连接
# db.commit() 提交到数据库执行
# db.rollback() 回滚
# cur = db.cursor() 返回游标对象,用于执行具体SQL命令
# 游标对象(cur)的方法
# cur.execute(sql命令,[列表]) 执行SQL命令
# cur.close() 关闭游标对象
# cur.fetchone() 获取查询结果集的第一条数据 (1,100001,"河北省")
# cur.fetchmany(n) 获取n条 ((记录1),(记录2))
# cur.fetchall() 获取所有记录

# pymysql使用流程
# 1. 建立数据库连接(db = pymysql.connect(...))
# 2. 创建游标对象(c = db.cursor())
# 3. 游标方法: c.execute("insert ....")
# 4. 提交到数据库 : db.commit()
# 5. 关闭游标对象 :c.close()
# 6. 断开数据库连接 :db.close()
import pymysql
# 1.创建数据库连接
db = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='123456',
    database='country',
    charset='utf8'

)
# 创建游标对象
cur= db.cursor()
# 生成一个列表
data_list=[]
for i in range(1,2000001):
    data_list.append('Tom{}'.format(str(i)))
print(len(data_list))

ins = 'insert into students(name) values(%s)'
# for i in range(1,2000001):
#     sql='insert into students(name) values(%s)'%i

cur.executemany(ins,data_list)
# 游标方法: c.execute("insert ....")
db.commit()
# 提交到数据库 : db.commit()
cur.close()
db.close()