# import pymysql.cursors
#
# connection = pymysql.connect(
#     host='127.0.0.1',
#     port=3306,
#     user='root',
#     password='123456',
#     db='test',
#     charset='utf8mb4',
#     cursorclass=pymysql.cursors.DictCursor
# )
#
# try:
#     with connection.cursor() as cursor:
#         sql = """SELECT * FROM shirt;"""
#         cursor.execute(sql)
#         result = cursor.fetchall()
#         print(result)
#         for row in result:
#             print('小红有一件{}色的{}'.format(row['color'], row['style']))
#
# except Exception as e:
#     print(e)
# finally:
#     connection.close()


import pymysql.cursors

connection = pymysql.connect(
    host= '127.0.0.1',
    port = 3306,
    user= 'root',
    password= '123456',
    db= 'test',
    charset= 'utf8mb4',
    cursorclass= pymysql.cursors.DictCursor
)


with connection.cursor() as cursor:
    sql="""SELECT * FROM shirt;"""
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result)
    for row in result:
        print('小红有一件{}色的{}'.format(row['color'], row['style']))

with connection.cursor() as cursor:
    sql1 = """SELECT id FROM person WHERE name='小明';"""
    cursor.execute(sql1)
    result = cursor.fetchall()
    print(result)
    xiaoming_id = result['id']

    sql = """UPDATE shirt SET color='黄' WHERE person_id=%s and style='风衣';"""
    cursor.execute(sql, (xiaoming_id))
    sss= cursor.fetchall()
    print(sss)
connection.commit()