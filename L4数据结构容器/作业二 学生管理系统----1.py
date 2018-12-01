## 1.学生列表结构为学生姓名组成的列表。

#要求：终端开始打印主菜单信息如下。提问用户选择哪种操作？
#     1—查询学员姓名
#     2--添加学员姓名
#     3--修改学员姓名
#     4--删除学员姓名
#     0--退出程序

student_list = ['小王','小红','小李']

while True:
    print ('1','查询学员姓名')
    print ('2','添加学员姓名')
    print ('3','修改学员姓名')
    print ('4','删除学员姓名')
    print ('0','退出程序')

    user_stud= int(input('请输入选择的序号：'))

    if user_stud == 1:
    #print(len(student_list))
        print('行号\t\t姓名')
        print('----------------')
        for i in range(0,len(student_list)):
            print(i +1,'\t\t',student_list[i])
    elif user_stud == 2:
        n_list=input('请输入要添加的姓名：')
        student_list.append(n_list)
        print(student_list)
        print('添加成功')
    elif user_stud == 3:
        i = int(input('请输入要修改的名字数字：'))
        s_list=input('输入修改后的名字:')
        student_list[i-1] = s_list
        print(student_list)
    elif user_stud ==4:
        a = int(input('请输入要删除第几个学生：'))
        student_list.pop(a-1)
        print(student_list)
    elif user_stud == 0:
        print('谢谢使用')
        break


##  子操作（4.删除）
    print("""请输入操作编号：
         1.按学生编号删除
         2.删除全部学生（谨慎)
    """)
    sub_num = int(input('请选择子操作：'))
    if sub_num ==1:
        stu_num = int(input('要删除第几个学生：'))
        student_list.pop(stu_num -1)
        print('删除成功')
    elif sub_num ==2:
        confirm = input('确认删除全部？（Y/N)')
        if confirm == 'Y' or confirm == 'y':
            student_list.clear()
            print('删除全部成功')



