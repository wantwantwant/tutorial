(重要)sql语法
===
之前已经学过create table, select、update、delete基础语句。下面排序、分组、统计、表连接。

## 语法
（频率高）：SELECT Company FROM Orders;
去重（频率中级）：SELECT DISTINCT Company FROM Orders ;
多个限定条件满足：SELECT * FROM Persons WHERE FirstName='Thomas' AND LastName='Carter';
多个限定条件满足其一：SELECT * FROM Persons WHERE firstname='Thomas' OR lastname='Carter';
排序SELECT Company, OrderNumber FROM Orders ORDER BY Company DESC;
排序SELECT Company, OrderNumber FROM Orders ORDER BY Company DESC, OrderNumber ASC;
取结果集10到20的条目：mysql中 select * from table limit 10,20;
取结果集前10的条目：select * from table limit 10; select top 10 * from table;
模糊取字段：SELECT * FROM Persons WHERE City LIKE 'N%'; %表示通配符，_匹配一个字符。 N%-匹配-New-NewYork, 
列的值在一个列表当中：SELECT * FROM Persons WHERE LastName IN ('Adams','Carter'); 注意效率。
别名：SELECT LastName AS Family, FirstName AS Name FROM Persons;


## 语法 join表连接
需求：设计订单表。第一次设计的order表含字段：id，order_no,person_name,price,person_address,person_vip,product_info。如果这样设计，发现问题，一是字段越来越多、各种维度信息混合在一起不好维护。二是product_list_info列表信息不好表达。
所以我们按字段分类设计成两张表。表一：person（name,address,vip,phone） 表二：order（id,order_no,price,person_id）
这里的person.id是'外键 foreign key'。外键的好处：分类清晰，保证数据一致性；缺点：影响效率。

SELECT Persons.LastName, Persons.FirstName, Orders.OrderNo
FROM Persons
INNER JOIN Orders
ON Persons.Id_P = Orders.Id_P
ORDER BY Persons.LastName;

SELECT Persons.LastName, Persons.FirstName, Orders.OrderNo
FROM Persons AS p
INNER JOIN Orders AS o
ON p.Id_P = o.Id_P;

INNER省略的话默认join就是inner join内连接。给表起别名减少代码量。
left join。左表中的列不管有木有匹配右边的表中数据，都会展示出左边表的数据行。right join相反以右表为主。full join笛卡尔积消耗资源，一般情况下主要inner join，少量left join，其他join几乎用不到用到再查。

## 管理数据库
创建schema库 CREATE DATABASE database_name;
新建表       CREATE TABLE 表名称（列名称1 数据类型，列名称2 数据类型，）
约束constrain  针对insert语句。   not null非空    unique唯一   主键  外键
索引 CREATE INDEX index_table_name ON table_name (column_name);  索引好像书本前的目录，空间换时间，增加建立索引那列的查询速度。
丢弃 DROP TABLE 表名称  删除张表结构和数据和索引，delete只删除数据。
修改 ALTER TABLE table_name ADD column_name datatype;

创建用户，权限等用到在查文档。

## 函数
平均值 avg（字段）
计数   count（字段）
时间   now（）
如果分组后统计   select * from table group by vip HAVING avg(字段);
SELECT Customer,SUM(OrderPrice) FROM Orders GROUP BY Customer
如果分组后还要跟条件筛选 不能用where 要用having

## 作业
作业2：了解sql语法
作业3： 准备mysql服务，确保正常登陆。
