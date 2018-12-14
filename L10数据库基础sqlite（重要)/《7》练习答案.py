# coding:utf-8
# __autor__:'cyb'

# 学生管理v4 sqlite版 （讲解）

import sqlite3

def create_table():
    connect = sqlite3.connect("testsqlite.db")
    cursor = connect.cursor()
    cursor.execute("""
       CREATE TABLE students
       (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(20) NOT NULL,
            sex VARCHAR(20),
            age INTEGER,
            phone VARCHAR(20)
       );
    """)
    connect.commit()
    cursor.close()
    connect.close()

def show_students():
    print('行号\t\t姓名\t\t年龄\t\t性别\t\t电话\t\t')
    print("-------------------------------------------------------")
    connect = sqlite3.connect("testsqlite.db")
    cursor = connect.cursor()
    cursor.execute("""
       SELECT * FROM students;
    """)
    student_list = cursor.fetchall()  #[(1,小明,年龄，性别，电话)]
    for index,student in enumerate(student_list):
        print(f'{index+1}\t\t\t{student[1]}\t\t\t{student[2]}\t\t\t{student[3]}\t\t\t{student[4]}')
    cursor.close()
    connect.close()
def add_student():
    name = input('新学生姓名：')
    sex = input('新学生性别：')
    age = input('新学生年龄:')
    phone = input('新学生电话:')

    connect = sqlite3.connect("testsqlite.db")
    cursor = connect.cursor()
    # sql = """
    #      INSERT INTO students(name,sex,age,phone) VALUES ("%S","%S",%S,"%S")"""%(name,sex,age,phone)
    sql = f"""
         INSERT INTO students(name,sex,age,phone) VALUES ("{name}","{sex}",{age},"{phone}");
    """

    cursor.execute(sql)
    connect.commit()
    connect.close()

    print('新学生添加成功')

def  update_student():
    number = int(input('要修改第几个学生：'))
    new_name = input('修改后的姓名是：')
    new_sex = input('修改后的性别：')
    new_age = int(input('修改后的年龄：'))
    new_phone = input('修改后的电话;')

    connect = sqlite3.connect("testsqlite.db")
    cursor = connect.cursor()
    sqli = f"""
        UPDATE students SET name="{new_name}",sex="{new_sex}",age={new_age},phone="{new_phone}" WHERE id={number};
    """

    cursor.execute(sqli)
    connect.commit()
    connect.close()

    print('学生修改成功')

def delete_student():
    print("""请输入子操作编号：
                1.按学生编号删除
                2.删除全部学生
           """)
    num = int(input('请选择子操作：'))
    if num == 1:
        stu_num = int(input('要删除第几个学生：'))
        connect = sqlite3.connect("testsqlite.db")
        cursor = connect.cursor()

        sqlit = f"""
            DELETE FROM students WHERE id={stu_num-1};
        """

        cursor.execute(sqlit)
        connect.commit()
        connect.close()

        print('删除成功')
    elif num ==2:
        confirm = input('是否全部删除？(Y/N)')
        if confirm == 'Y'or confirm =='y':
            connect = sqlite3.connect("testsqlite.db")
            cursor = connect.cursor()
            sqlite = f"""
               DELETE FROM students;
            """

            cursor.execute(sqlite)
            connect.commit()
            connect.close()

            print('全部删除成功')


def main():
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
             add_student()
        elif num ==3:
            update_student()
        elif num ==4:
            delete_student()
        elif num ==0:
            break

if __name__ == '__main__':
    main()


