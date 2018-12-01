# 学生管理系统——v2
# tip:pycharm左侧的structure可以看脚本结构。

student_list =[
               {'name': '小明', 'age':10, 'sex':'male'},
               {'name':'小红', 'age':12, 'sex':'female'},
               {'name':'小李', 'age':12, 'sex':'male'}
               ]

def show_students():
    print('行号\t\t姓名\t\t年龄\t\t性别\t\t')
    #print('{:<10}{:<10}'.format('行号'))
    print('---------------------------------')
    for i in range(0,len(student_list)):
        stu_dict=student_list[i]
        name=stu_dict['name']
        age=stu_dict['age']
        sex=stu_dict['sex']
        print('{}\t\t{}\t\t{}\t\t{}'.format(i+1,name,age,sex))

def add_student():
    show_students()
    new_name=input('请输入要添加的学生的新姓名：')
    new_age=input('请输入要添加学生的年龄：')
    new_sex=input('请输入要添加的学生的性别：')

    new_stu_dict={
        'name':new_name,
        'age':new_age,
        'sex':new_sex
    }
    student_list.append(new_stu_dict)
    print('添加成功')

def update_student():
    show_students()

    num=int(input('要修改第几个学生：'))
    new_name=input('修改后的姓名是：')
    new_age=int(input('修改后的年龄是：'))

    student_list[num-1]['name']=new_name
    student_list[num-1]['age']=new_age
    print(student_list)
    print('修改成功')

def delete_student():
    print("""请输入子操作编号：
             1.按学生编号删除
             2.删除全部学生
        """)
    num=int(input('请选择子操作：'))
    if num ==1:
        stu_num=(input('要删除第几个学生：'))
        student_list.pop(stu_num-1)
        print('删除成功')
    elif num ==2:
        confirm=input('是否全部删除？（Y/N）')
        if confirm =='Y'or confirm =='y':
            student_list.clear()
            print('删除成功')




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
             add_student()
        elif num ==3:
            update_student()
        elif num ==4:
            delete_student()
        elif num ==0:
            break