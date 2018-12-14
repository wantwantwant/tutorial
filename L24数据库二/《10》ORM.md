ORM
===
引题：学完pymysql后大家已经可以写学生管理系统的mysql数据库版本了，类似sqlite版本。
步骤: 设计数据库；数据库图形工具中或py脚本中创建数据库表；开发；
发现缺点：纸上、或画ER图，写sql，图形工具中运行sql创建表 2>数据取出来之后需要声明一些变量来接收。这些变量与student类类似。重复 3> 如果要修改表结构


## rom
ORM: object relational mapping  对象关系映射。类映射数据库表。类似wtform从后端类生成前端html代码,orm框架会从类生成sql并执行。查询时不需要写sql直接通过类对象，只需要维护后端python代码，思维专注。
知名的orm框架：sqlAlchemy（重）， django中集成的orm， peewee(轻量)。
优点：提高开发效率，代码风格统一为后端。
缺点;由于封装，