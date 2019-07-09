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

while True:
    # name=input("Name:")
    # age=int(input("Age:"))
    # gender=input("Sex:")
    # score=float(input("Score:"))

    name = input("Name:")
    age = input("Age:")
    gender = input("Gender:")
    score = input("Score:")

    # sql="insert into myclass (name,age,gender,score) values ('%s',%d,'%s',%f);"\
    # %(name,age,sex,score)

    sql="insert into myclass (name,age,gender,score) values (%s,%s,%s,%s);"


    # print(sql)

    try:
        cur.execute(sql,[name,age,gender,score])
        db.commit()
    except Exception as e:
        db.rollback() # 失败回滚到操作之前的状态
        print("Faild:",e)

    else:
        print("死鬼操作成功")

