# 学生管理v1-函数封装
# 之前的非函数版本，打印学生列表代码重复，如果要修改需要
#    处处修改。while if 嵌套，代码越来越长，不容易维护。所
#    以我们封装成。

student_list = ['小王','小红','小李']

def show_students():
    # print(len(student_list))
    print('行号\t\t姓名')
    print('----------------')
    for i in range(0, len(student_list)):
        print(i + 1, '\t\t', student_list[i])
def add_student():
    n_list = input('请输入要添加的姓名：')
    student_list.append(n_list)
    print(student_list)
    print('添加成功')
def update_student():
    show_students()

    stu_num = int(input('修改第几个：'))
    student_list[stu_num -1]=input('修改后的名字：')
    print('修改成功')

def delete_student():
    print("""请输入操作编号：
             1.按学生编号删除
             2.删除全部学生（谨慎)
        """)

    sub_num = int(input('请选择子操作：'))

    if sub_num == 1:
        stu_num = int(input('要删除第几个学生：'))
        student_list.pop(stu_num - 1)
        print('删除成功')
    elif sub_num == 2:
        confirm = input('确认删除全部？（Y/N)')
        if confirm == 'Y' or confirm == 'y':
            student_list.clear()
            print('删除全部成功')

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


# if _name_ == '_main_':  # 这种写法含义将会在'包，模块'中的一节课中介绍。
    main()
