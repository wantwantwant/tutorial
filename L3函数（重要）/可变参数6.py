# （了解）可变参数

# 引题：有些函数的参数比较多，都写出来比较长不方便写和看：传实参的个数不确定。
def print_stu_info(name='',age='',sex='',score='',address='',phone=''):
    pass

def get_max_num(a,b,c,d,e,f,g):
    pass

# 上面的参数a,b,c,d,e,f,g结构有点像列表，所以Python就提空一种方便表示
#    固定数量参数的语法。
# 可变列表参数：起一个形参名来接收列表，列表的每一项都是参数，多个参数组成列表。为了标示这个形参是特别，
#    前面有个*号。
argumens=['小明','小红','小李','小青']
def print_stu_info(*args):
    print(args)
    for i in args:
        print(i)
    # 拿到参数后在函数体内继续进行运算。

print_stu_info(*['小明','小红','小李','小青'])

# 这个例子只传入了一个参数。参数类型为列表。上面的例子传入的是不同方面的参数
#      只不过用列表把他们装在一起，本质是传入多个参数。
def print_stu_info4():
    for i in 1:
        print(i)
print_stu_info4(['小明','小红','小李','小青'])


# 可变字典参数：
def print_stu_info2(**kwargs):
    print(kwargs)
    print(kwargs['name'])
    print(kwargs['age'])

print_stu_info2(**{'name':'小明','age':10,'sex':'male','score':90})
# 可变参数好处：参数变量可变，修改方便。代码量比较少。
#     逻辑都在函数中，代码整体可读性好。

# 可变参数的位置.字典参数必须要在列表参数之后。
def print_stu_info3(a,b,*args,**kwargs):
    pass
print_stu_info3()

# 面试：函数中有哪几种参数？顺序有木有要求？

# 位置参数、可变参数、默认参数、键值对参数。
# 参数的顺序：默认参数 必须要在 位置参数之后。