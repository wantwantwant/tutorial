# coding:utf-8
# __autor__:'cyb'

import sqlite3
connect = sqlite3.connect("testsqlite.db")
cursor = connect.cursor()
cursor.execute("""
      SELECT id,name,sex,phone from employee;
""")
employee_list = cursor.fetchall()
print(employee_list)

cursor.execute("""
     INSERT INTO employee (name,sex,phone) VALUES ("张三","male",13244559933);
""")

cursor.execute("""
    SELECT * FROM employee;
""")
employee = cursor.fetchall()
print(employee)

cursor.execute("""
   SELECT * FROM employee WHERE sex = '男';
""")
# fetchall全部读出 fetchone 只读一个
employee1 = cursor.fetchall()
print(employee1)

cursor.execute("""
   UPDATE employee SET phone=14563456778 WHERE name='张四';
""")

connect.commit()

# cursor.execute("""
#    DELETE FROM employee WHERE name='张三';
# """)
#
# connect.commit()
# 假性删除，为了防止数据误删除和方便找回，专门新建一个标识字段表示用户状态（正常，注销）
cursor.execute("""
   update employee set del_flag=1 where name='张二';
""")
connect.commit()
cursor.execute("""
   select * from employee where del_flag=0;
""")

connect.close()
