## 学生管理系统（v2字典）

students =[{'name': '小明', 'age':10, 'sex':'male'},
           {'name':'小红', 'age':12, 'sex':'female'},
           {'name':'小李', 'age':12, 'sex':'male'}
          ]

while True:
    print("""
            1-查询学员姓名
            2-添加学员姓名
            3-修改学员姓名
            4-删除学员姓名
            0-退出程序""")
    num = int(input('请选择操作序号：'))
    if num==1:
        #def show_students():
        print('行号\t\t姓名\t\t年龄\t\t性别')
        print('----------------------------------------')
        for i in range(0,len(students)):
            #students.values('name','age','sex')
            print(i+1,'\t\t',students[i]['name'],'\t\t',students[i]['age'],'\t\t',students[i]['sex'])

    elif num==2:
        a_list =input('请输入要添加的学生的姓名:')
        b_list = int(input('请输入要添加的学生的年龄:'))
        c_list = input('请输入要添加的学生的性别:')

        new_stu_dict={'name':a_list,'age':b_list,'sex':c_list}

        students.append(new_stu_dict)
        print('添加完毕')
    elif num==3:
        e=int(input('请输入要修改第几个名字：'))
        f_list=str(input('请输入要修改后的名字：'))
        g_list=str(input('请输入要修改后的年龄：'))
        h_list=str(input('请输入要修改后的性别：'))
        students[e-1]={'name':f_list,'age':g_list,'sex':h_list}
        print(students)
    elif num==4:
        print("""请输入操作序号
                1-按学生编号删除
                2-删除全部学生
            """)
        sub_num=int(input('请选择子操作：'))
        if sub_num == 1:
            stu_num = int(input('要删除第几个学生：'))
            students.pop(stu_num - 1)
            print('删除成功')
        elif sub_num == 2:
            confirm = input('确认删除全部？（Y/N)')
            if confirm == 'Y' or confirm == 'N':
                students.clear()
                print('删除全部成功')
    elif num==0:
        print('谢谢使用')
        break






