# 格式化输出

# 简单输出
print('你好小明')
print('你好小红')
print('你好小李')

# 带变量的输出
# 更有灵活性，好处参考excercisel-3
name = '小明'
print(name)

# 加好拼接字符串
pay = 8
print('花费一共' + pay +'元')

# print里用逗号打印多个变量
name = '小明'
score = '90'
print(name,score)
print('学生姓名：' + name + ',学生成绩：' + str(score))

# 但是，变量较多,加号拼接字符串比较麻烦
name = '小明'
score = 90
sex = 'male'
height = 180
weight = 70
address = '郑州市xx街道'
phone = '137331779926'
print = '1111111111111111111111111111111'

# 所以，我们使用格式化输出字符串
# 方法一：'姓名%s，成绩%s' % (变量1，变量2）
# %s 是占位符，将要被变量填充。
# %s 字符串，%d 整数，%f 浮点数
# C语言写法，并不推荐这种写法，但很多项目还在使用，要求看懂。
print('学生姓名%s,成绩%d' % (name,score))

# （重点）方法二：format()
# 优点：不用转型。面向对象使用自然。
print('学生姓名{}，成绩{}'.format(name,score))
# 参数较多时可以给占位符起变量名
print('学生姓名{stu_name}，成绩{stu_score}'.format(stu_name='小明',stu_score=90))
# 小数点精度
print('河南省面积{：.2f}'.format(190.5832))
# 左对齐右对齐
print('{:`20}'.format('对齐'))
print('{:<20}'.format('对齐'))
print('{:>20}'.format('对齐'))

# print()输出后不换行
'12'
print('1')
print('2')

print('1',end='')   # 光标就不会换行

#(重点) f-string   py3.6新加入
# 优点：变量插值更加直观灵活，动态计算速度快。
name = '小明'
age = 13
print(f'学生姓名：{name}，年龄{age}')