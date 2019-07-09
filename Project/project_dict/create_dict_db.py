import pymysql
import re

# 1. 建立数据库连接(db = pymysql.connect(...))
db = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='123456',
    database='dict_mysql',
    charset='utf8'
)

# 2. 创建游标对象(c = db.cursor())
# 获取游标
c = db.cursor()

fd = open('dict.txt')
# while True:
for line in fd:
    data=re.search(r'\S+',line).group()
    # print(data)
    data1=line[len(data):].lstrip()
    # print(data1)
    # break
    temp="insert into words (word,mean) values (%s,%s);"

    c.execute(temp,[data,data1])

# # 查询
# while True:
#     data=input(">>>")
#     if not data:
#         break
#     temp="select * from Word where word = %s;"
#
#     c.execute(temp,[data])
#
#     word=c.fetchone()
#     if not word:
#         print("Not Found")
#         continue
#     print(word[2])
db.commit()
# 5. 关闭游标对象 :c.close()
c.close()
# 6. 断开数据库连接 :db.close()
db.close()
# fd.close()
