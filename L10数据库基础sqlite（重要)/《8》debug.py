# coding:utf-8
# __autor__:'cyb'
#import pdb
# def test(arg):
#     for i in range(arg):
#         print(i)
#     return arg
# test(3)

"""
断点：debug运行到某一句代码时暂时停住。一句一句向下执行太慢，我们只需要在可能出现问题的代码前设置断点。
1.运行程序
2.（pdb）模式下 输入”c“回车，程序会执行到第一个断点处。信息提示，运行到第几行，在哪个函数哪个文件下。
3.（pdb）模式下 输入”1“回车，查看断点周围代码
4.（pdb）模式下 输入”s“回车，向下执行一句代码
5.（pdb）模式下 输入”a“回车，查看相关变量的值

debug好处：代码一句一句执行，不断查看变量的值，为编程提供信息支持。
pdb缺点：打断点不方便，命令行调试不方便。
"""

"""
为了使debug更加方便，pycharm提供了图形化工具。
1.编辑器左侧行号区域，单击设置断点
2.似debug模式运行
"""


def test2(arg):
    for i in range(arg):
        print(i)
    return arg
test2(10)

def test3():
    while True:
        print('hello')
    print('world')
test3()