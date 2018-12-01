# 捕获异常
# 场景：一个大型项目，业务逻辑复杂。当出现异常错误的时候
#     我们并不希望程序终止，希望程序主题功能运行；收集分
#     析错误信息。

# 捕获异常  （重点）
def foo():
    try:
        print(1/0)
    except ZeroDivisionError:
        print('不能除以0')
    finally:
        print('我最后执行')
    print('world')

def boo():
    print('hello')
    foo()
    print('world')

boo()

"""
(重点）捕获异常：try..except..finally
try括住可能发生问题的语句。偷懒方法try括住程序最外层，但这样
  捕获后不好定位出错地方。
except 后面跟异常的类名，如果捕获到这种异常，那么就会执行语句
  块中的内容，执行发生异常后的一些处理，处理比如 用户提示信息、
  记录日志、业务逻辑。
finally 不管程序正常运行，或是出现某种异常被捕获，再或是出现
  异常没有被捕获到，最终都会执行。
  
捕获异常应该适当使用，使用过多代码会乱，不用的话错误可能导致
  程序崩溃带来损失。场景：捕获数据库操作代码。
"""

# 示例2
try:
    f = open('demo.txt',encoding='gbk')
    content = f.read()
    print(content)   # try块里面的变量变成局部变量，注意外部不要饮用内部局部变量。
except FileExistsError:
     print('文件名未找到，请检查文件名')
except UnboundLocalError:
     print('unicode解码错误')
except Exception as e:
    print(e)
finally:
    f.close()

"""
try块里面的变量变成全局变量，注意外部不要引用内部局部变量。

如果try块中的代码可能报多种异常，那么多写几个并列的expect语句。

不知道错误类的类名；可能会出现代码中定义之外的未知错误。使用所有错误类的父类Exception类来捕获。
   
finally 场景：打开文件资源，不管有没有出错，最终应该保证关闭文件。
 
as:把...作为...,类似等号赋值，可以写成一行
"""