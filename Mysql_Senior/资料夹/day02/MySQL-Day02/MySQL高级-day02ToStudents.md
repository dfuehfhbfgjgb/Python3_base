# MySQL高级-Day01回顾

- **SQL查询总结**

```mysql
    3、select ...聚合函数 from 表名
    1、where ...
    2、group by ...
    4、having ...
    5、order by ...
    6、limit ...;
```

- **聚合函数（铁三角之一）**

avg(...) sum(...) max(...) min(...) 
count(字段名)  # 空值NULL不会被统计

- **group by（铁三角之二）**

给查询结果进行分组
如果select之后的字段名和group by之后的字段不一致,则必须对该字段进行聚合处理(聚合函数)

- **having语句（铁三角之三）**

对查询的结果进行进一步筛选
**注意**
1、having语句通常和group by语句联合使用,过滤由group by语句返回的记录集
2、where只能操作表中实际存在字段,having可操作由聚合函数生成的显示列

- **distinct** 

select distinct 字段1,字段2 from 表名;

- **查询时做数学运算**

select 字段1*2,字段2*3 from 表名;

- **索引(BTree)**

优点 ：加快数据检索速度
缺点 ：占用物理存储空间,需动态维护,占用系统资源
SQL命令运行时间监测
		1、开启 ：mysql> set profiling=1;
		2、查看 ：mysql> show profiles;
		3、关闭 ：mysql> set profiling=0;

- **普通(MUL)、唯一(UNI,字段值不能重复,可为NULL)**

  **创建**
  		index(字段名),index(字段名)
  		unique(字段名),unique(字段名)
  

​		自定义索引

  ​		create [unique] index 索引名 on 表名(字段名);

  **查看**
  		desc 表名;
		show index from 表名\G;  
  			Non_Unique:1 :index
  			Non_Unique:0 :unique

  **删除**
  		drop index 索引名 on 表名; (只能一个一个删)

# MySQL高级-Day02笔记

## **外键（见Day01笔记）**

## **多表查询（见Day01笔记）**

## **连接查询（见Day01笔记）**

## **数据导入**

**作用**

把文件系统的内容导入到数据库中
**语法（方式一）**

load data local infile "文件名"
into table 表名
fields terminated by "分隔符"
lines terminated by "\n"
**示例**
scoretable.csv文件导入到数据库db2的表aid1903中

```
1、将scoretable.csv放到数据库搜索路径中
mysql>show variables like 'secure_file_priv';
sudo cp scoreTable.csv /var/lib/mysql-files/
2、在数据库中创建对应的表
create table scoretab(
rank int,
name varchar(20) not null,
score float(5,2), 
hone char(11),
lass char(7)
)charset=utf8;
3、执行数据导入语句
load data infile '/var/lib/mysql-files/scoreTable.csv' 
into table scoretab 
fields terminated by ',' 
lines terminated by '\n';

4.添加id字段，要求主键自增长，宽度为3，不足0补上。
alter table scoretab add id int(3) zerofill primary key auto_increment first;

```

**语法（方式二）**

source 文件名.sql

## **数据导出**

**作用**

将数据库中表的记录保存到系统文件里

**语法格式**

select ... from 表名
into outfile "文件名"
fields terminated by "分隔符"
lines terminated by "分隔符";

**练习**

```mysql
把sanguo表中英雄的姓名、攻击值和国家三个字段导出来,放到 sanguo.txt中
select name,attack,country from sanguo 
into outfile '/var/lib/mysql-files/sanguo.csv' 
fields terminated by ',' 
lines terminated by '\n';
将mysql库下的user表中的 user、host两个字段的值导出到 user2.txt，将其存放在数据库目录下
select user,host from mysql.user into outfile '/var/lib/mysql-files/user2.txt'  fields terminated by '    '  lines terminated by '\n'; 
查看user2.txt
mysql> system sudo cat /var/lib/mysql-files/user2.txt
```

**注意**

```
1、导出的内容由SQL查询语句决定
2、执行导出命令时路径必须指定在对应的数据库目录下
```

## **表的复制**

**语法**

```mysql
create table 表名 select 查询命令;

```

**练习**

```mysql
1、复制sanguo表的全部记录和字段,sanguo2
create table sanguo2 select * from sanguo;
2、复制sanguo表的前3条记录,sanguo3
create table sanguo3 select * from sanguo limit 3;
3、复制sanguo表的 id,name,country 三个字段的前3条记录,sanguo4
create table sanguo4 select id,name,country from sanguo limit 3;
```

**注意**

复制表的时候不会把原有表的 键 属性复制过来

**复制表结构passwd**
create table 表名 select 查询命令 where false;

## **锁**(MySQL自动加锁和释放锁)

**目的**

解决客户端并发访问的冲突问题

**锁类型分类**

读锁(共享锁) ：select 加读锁之后别人不能更改表记录,但可以进行查询
写锁(互斥锁、排他锁) ：加写锁之后别人不能查、不能改

**锁粒度分类**

表级锁 ：myisam
行级锁 ：innodb

## **存储引擎**



**基本操作**

```mysql
1、查看所有存储引擎
2、查看已有表的存储引擎
3、创建表时指定存储引擎
4、已有表指定存储引擎
```

**常用存储引擎特点**

InnoDB特点
			

```mysql
1、支持行级锁
2、支持外键、事务操作
3、表字段和索引同存储在一个文件中
```

MyISAM特点

```mysql
1、支持表级锁
2、表字段和索引分开存储
```

**如何决定使用哪个存储引擎**

```
1、执行查操作多的表用 MyISAM
2、执行写操作多的表用 InnoDB
```

## **MySQL的用户账户管理**

**开启MySQL远程连接**

```mysql

```

**添加授权用户**

```mysql
1、用root用户登录mysql
	mysql -uroot -p123456
2、授权
	grant 权限列表 on 库.表 to "用户名"@"%" identified by "密码" with grant option;
```

**权限列表**

all privileges 、select 、insert ... ... 

库.表 ： * . * 代表所有库的所有表

**示例**

```mysql
1、添加授权用户tiger,密码123,对所有库的所有表有所有权限
grant all privileges on *.* to tiger@"%" identified by "123" with grant option;
mysql> grant all privileges on *.* to 'root'@'%' identified by '123456' with grant option;
说明：此命令是为密码为 root 、IP（%）任意的 root 用户授权。（%：模糊查询，所有 IP 都可以,，可指定其他主机 IP；BY 后的 'root' 为密码）
将配置写入 mysql 授权表中
mysql> flush privileges;
修改mysql库的user表，将host项，从localhost改为%。%这里表示的是允许任意host访问，如果只允许某一个ip访问，则可改为相应的ip，比如可以将localhost改为192.168.1.123，这表示只允许局域网的192.168.1.123这个ip远程访问mysql。
mysql>use mysql; 
mysql>update user set host = '%' where user ='root';
mysql>select host,user from user;
mysql> flush privileges;
补充：防火墙开放3306端口

2、添加用户rabbit,对db2库有所有权限

```

# 今日作业

1、把 /etc/passwd 文件的内容导入到数据库的表中

进入mysql下的/var/lib/mysql-files/

sudo -i

cd /var/lib/mysql-files

ls

vi /etc 进入etc目录下

ls 可查找到passwd



vi /etc/passwd 查看passwd内容

ctrl+z 退出vi界面



​	1、将passwd复制到数据库搜索路径中

​	sudo cp /etc/passwd /var/lib/mysql-files/

或在mysql 环境下执行

​	system sudo cp /etc/passwd  /var/lib/mysql-files/

​	2、在数据库中创建对应的表

   create table dates(A varchar(64),B char(1),C int(5),D int(5),E text,F text,G text)charset=utf8;

​	3、执行数据导入语句

	load data infile '/var/lib/mysql-files/passwd'
	into table dates
	fields terminated by ':'
	lines terminated by '\n';
	4.添加id字段，要求主键自增长，宽度为3，不足0补上。

​	alter table dates add id int(3) zerofill primary key auto_increment first;