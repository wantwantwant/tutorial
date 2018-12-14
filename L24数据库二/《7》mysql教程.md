                                                                                                                                                                                                                                  mysql官网入门教程
===
## 步骤
1.启动服务  shell>mysqld
2.客户端 shell>mysql --help
3.客户端登录 mysql -u root -p
如果服务器在另一台计算机 需要ip地址和端口参数mysql -h 127.0.0.1 -P 3306 -u root -p
4.执行各种sql

## sql
select version(), current_date();
关键字大小写都行，函数可以省略(),每句分号结尾。
current database 库名；
刚连接mysql后，mysql只有几个保存系统信息的内置数据库（表信息 权限信息）我们不应该所以动内置库。schema是逻辑上的大分块，schema下包含库，当有一个项目想保存信息时，我们需要先新建一个库 database，然后在database下新建表，表里村信息。有些数据库中schema和database一样。
