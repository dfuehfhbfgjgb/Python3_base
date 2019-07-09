"""
    数据库
    二进制存储文件
"""
import pymysql

# 创建连接
db = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='123456',
    database='stu',
    charset='utf8'
)


# 创建游标
cur= db.cursor()

# # 存储文件
# with open ('bitree1.jpg','rb') as fd:
#     data=fd.read()
# try:
#     sql= "insert into Images values (1,'bitree1.jpg',%s);"
#     cur.execute(sql,[data])
#     db.commit()
# except Exception as e:
#     db.rollback()
#     print(e)


# 获取文件
sql="select * from Images where filename='bitree.jpg';"

cur.execute(sql)
image = cur.fetchone()

with open(image[1],'wb') as fd:
    fd.write(image[2])

cur.close()
db.close()



