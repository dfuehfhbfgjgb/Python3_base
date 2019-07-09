"""
    写数据库操作
    增、删、改
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

try:
    # sql="insert into interest values (7,'Lily','draw,sing','A','8888','凑合吧');"
    # cur.execute(sql)
    # db.commit()
    sql = "update interest set price = 6666 where name = 'Bob';"
    cur.execute(sql)
    db.commit()
    sql = "delete from myclass where score < 80;"
    cur.execute(sql)
    db.commit()

except Exception as e:
    db.rollback()  # 失败回滚到操作之前的状态
    print("Faild:", e)
else:
    print("操作成功")