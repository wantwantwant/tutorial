# 判断变量类型

#类型不同，input（）返回字符串
# '1' + 3

# type(),  判断变量类型
a = 1
b = 1.5
c = 'hello'
d = True
type(a)   # <class'int'>
type(b)   # <class'float'>
type(c)   #<class'str'>
type(d)   #<class'bool'>


# isinstance（值，类型）
# 如果值属于类型的话返回True
isinstance(1,int)  # True
isinstance(1,float)  # False
isinstance('小明',float)  # False

