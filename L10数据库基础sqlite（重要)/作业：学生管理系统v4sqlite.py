# coding:utf-8
# __autor__:'cyb'
import sqlite3
connect = sqlite3.connect("testsqlite.db")
cursor = connect.cursor()

def show_students():
    cursor.execute("""
        SELECT * FROM students WHERE id>0;
    """)
    employee = cursor.fetchall()
    print(employee)

def add_students():
    show_students()
    new_name=input('请输入要添加的学生的新姓名：')
    new_age=int(input('请输入要添加学生的年龄：'))
    new_sex=input('请输入要添加的学生的性别：')
    new_phone = int(input('请输入要添加的学生的电话：'))

    insert_sql="INSERT INTO students (name,sex,age,phone) VALUES ('%s','%s',%s,'%s')"%(new_name, new_sex, new_age, new_phone)
    cursor.execute(insert_sql)
    connect.commit()
    connect.close()

    print('添加成功')

def update_students_info():
    show_students()

    select_number=int(input('要修改第几个学生：'))
    new_name = input('修改后的姓名是：')
    new_sex = input('修改后的性别：')
    new_age = int(input('修改后的年龄是：'))
    new_phone = input('修改后的电话：')
    update_sql = "UPDATE students SET name='%s',sex='%s',age=%s,phone='%s' WHERE id=%s"%(new_name,new_sex,new_age,new_phone,select_number)

    cursor.execute(update_sql)
    connect.commit()

    print('修改成功')

def delete_students():
    print("""请输入子操作编号：
             1.按学生编号删除
             2.删除全部学生
        """)
    num=int(input('请选择子操作：'))
    if num ==1:
        stu_num = int(input('要删除第几个学生：'))
        del_sql = "DELETE FROM students WHERE id=%d"%(stu_num-1)

        cursor.execute(del_sql)
        connect.commit()
        connect.close()

        print('删除成功')
    elif num ==2:
        confirm=input('是否全部删除？（Y/N）')
        if confirm =='Y'or confirm =='y':
              dele_sql = "drop table students";

              cursor.execute(dele_sql)
              connect.commit()
              connect.close()

              print('全部删除成功')




#def main():
while True:
        print ('1','查询学员姓名')
        print ('2','添加学员姓名')
        print ('3','修改学员姓名')
        print ('4','删除学员姓名')
        print ('0','退出程序')

        num = int(input('请输入选择的序号：'))

        if num == 1:
            show_students()
        elif num ==2:
             add_students()
        elif num ==3:
            update_students_info()
        elif num ==4:
            delete_students()
        elif num ==0:
            break