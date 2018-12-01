# 学生管理系统v3 类封装

student_list = [
    {'name': '小明', 'age': 10, 'sex': 'male'},
    {'name': '小红', 'age': 12, 'sex': 'female'},
    {'name': '小李', 'age': 12, 'sex': 'male'}
]

class Student():
    def show_students(self):
        print('行号\t\t姓名\t\t年龄\t\t性别\t\t')
        print('-------------------------------------------')
        for i in range(0,len(student_list)):
            print(i + 1,'\t\t\t',student_list[i]['name'],'\t\t',student_list[i]['age'],'\t\t',student_list[i]['sex'])

    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
        student_list.append(self.name,self.age,self.sex)
        print('添加完毕')

    def update_student(self):
        student_list[num - 1]['name'] = new_name
        student_list[num - 1]['age'] = new_age
        print(student_list)
        print('修改成功')

    def delete_student(self):
        print("""请输入子操作编号：
                     1.按学生编号删除
                     2.删除全部学生
                """)
        num = int(input('请选择子操作：'))



while True:
    print('1', '查询学员姓名')
    print('2', '添加学员姓名')
    print('3', '修改学员姓名')
    print('4', '删除学员姓名')
    print('0', '退出程序')

    num = int(input('请输入选择的序号：'))

    if num == 1:
        Student.show_students()
    elif num == 2:
        name=input('新的学生姓名')
        age=input('新的学生年龄')
        sex=input('新学生性别')
        Student=(name,age,sex)

    elif num == 3:
        num = int(input('要修改第几个学生：'))
        new_name = input('修改后的姓名是：')
        new_age = int(input('修改后的年龄是：'))
        Student.update_student()
    elif num == 4:
        Student.delete_student()
    elif num == 0:
        break












