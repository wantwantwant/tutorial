# coding:utf-8
# __autor__:'cyb'

# 数据库图形管理工具

"""
## 常用数据库图形管理工具
1.navicat系列   navicat for sqlite
优点navicatForMysql用户多  表多的时候界面方便，缺点是一是付费二是体验一般。
2.datagrip     jetbrains出品，优点一个软件连接多个数据库；操作习惯用pycharm类似，pycharm pro集成。缺点用户少；驱动不好下。
"""

"""
datagrip操作方法(pycharm集成database工具为例子）：
1.pycharm左下角图标调出工具栏，打开pycharm右侧database工具。
2.点加号-DataSourse数据源-sqlite
3.弹出的对话框选择drivers-sqlite（Xerial）
4.点击download sqlite-jdbc[latest]
5.如果网速不好的话，下载sqlite-jbdc-3.20.1.jar。对话框+号-custom jars 从本地安装
6.驱动安装成功后点击apply应用

7.点击对话框  project data source，开始配置连接数据库的实例
8.File路径点击...图标，选择要连接的.db文件。
9.点test connection，successful为成功
10.点击ok退出，看到连接的数据库实例下有表。

（了解)
JDBC:java操作数据库的驱动包。因为pycharm、datagrip是用java开发的。
.jar：java的代码包。
"""
"""
database工具使用：
展开目录，找到 表。

"""



"""
作业一（课下） ：课下下载navicat for sqlite，破解，连接数据库
作业二（课下): 课下下载datagrip ，破解，连接数据库 。http://www.jetbrains.com/datagrip/?fromMenu
作业三：连接上sqlite数据库，尝试新建表、新建字段、删除表。

"""