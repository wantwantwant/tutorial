#  第七题
user_number = ('x')
user_number = input('请输入一个数字：')
user_number = int(user_number)
if ('x % x==0'and'x % 1==0'):
    print('那么这个数为质数')




# 提示，列如数字15，分别除以1，2，3，4，。。。。15
# for num in range(1,100)
num = 14    # 待判断的量
total = 0    # 可以被整除的次数

if num == 1:
    print('1既不是质数也不是合数')
for i in range(1,15):
    if num % i == 0:
        total = total + 1
# 能被1和自身整除
if total == 2:
    print(num,'质数')
# 能被1、自身、和其他数整除
elif total> 2:
    print(num,'合数')








