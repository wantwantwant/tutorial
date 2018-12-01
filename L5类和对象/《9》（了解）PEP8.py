#（了解）PEP8代码风格指导


"""
PEP8 意思 Python增强方案第8号文件，这个文件说明了Python语言代码应该
   怎么书写，指导了书写风格，如果你的代码没有做到文件要求时，
   pycharm会报灰线提示。没有完全遵守规则不影响代码执行。但是建议遵守。

"""

# 操作符前后应该有一个空格
a=3
a = 3
# 方法与方法间有两个空行
def foo():
    pass


def boo():
    pass
# 类中的方法应该相隔一行
class Student(object):
    def foo(self):
        pass

    def boo(self):
        pass

# 类与类之间空两行
# 如果没有父类不写括号
# 类名应该用驼峰风格，每个单词首字母大写
class aaa():
    pass


class Bbb:
    pass
# 方法名、类名不要重复使用
def boo():
    pass
# 两个条件有时候可以写成链式
if 1<a and a<2:
    pass
if 1 < a < 2:
    pass
# 不建议代码写的过长，80个字符，pycharm的提示灰线在120字符

# 文件末尾代码结束时另起一新行
print('end')

"""
pycharm 有关代码风格操作
1.界面右下角图标点击，调节提示出现的级别（不提示、语法、拼写）
2.自动格式化代码快捷工具，界面左上菜单code/reformat code。
"""
