# mysql驱动
# 引题：已经学习了mysql语法，sqlite驱动操作sqlite数据库，datagrip的jsbc java驱动操作mysql。所以我们要找python操作mysql驱动

"""
驱动选择：
1.MySQLDB 已经有C驱动的mysql的成熟包，Mysqldb包python对这个c驱动包安装。优点是效率高，py2环境和众多项目中使用。缺点：windows下安装报错。可以在网上找对应平台编译后的.whl安装（也会出错）。终极解决方案是：去mysql官网下载对应平台的connect.msi安装。pip install MySQL-python
2.mysql-connector  python书写，类似MySQLdb但不依赖C语言驱动。
2.pymysql。纯python写的。缺点效率稍低。优点安装方便，完全兼容mysqldb的语法。市场占有越来越高。
"""

import pymysql.cursors

connection = pymysql.connect(host='127.0.0.1',
                             port=3306,
                             user='root',
                             password='123456',
                             db='test',
                             charset='utf8mb4', # 可以省略，8.0客户端默认utf-8可以省略，5.x最好带上
                            cursorclass = pymysql.cursors.DictCursor # 返回字典格式的结果集，不写返回默认元组格式。
                             )

try:
    with connection.cursor() as cursor:
        sql = """SELECT * FROM shirt;"""
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
        for row in result:
            print('小红有一件{}色的{}'.format(row['color'], row['style']))

    # with connection.cursor() as cursor:
    #     #     sql = """INSERT INTO shirt values (%s, %s, %s, %s)""".format()
    #     #     affected_rows = cursor.execute(sql, (None, '裙子', '红', 2))
    #     #     print(affected_rows)
    #     # connection.commit()

except Exception as e:
    print(e)
finally:
    connection.close()

# 扁平写法
# cursor = connection.cursor()
# cursor.exe()
# cursor.fetchone()
# cursor.close()
# connection.close()
