# 引题
## 需求：已知圆的半径为2cm，算这个圆的面积。
r = 2
print(3.14 * r * r)
##需求2：已知三个圆的半径分别为1cm，3.5cm，10cm，求这三个圆的面积。
r1 = 1
r2 = 3.5
r3 = 10
print('圆的面积',3.14 * r1 * r1)
print('圆的面积',3.14 * r2 * r2)
print('圆的面积',3.14 * r3 * r3)

# 上面的代码重复，工作越来越多，
# 函数function：将重复的代码抽象出来，多次调用，这就是函数。
# 封装代码（函数化），函数把业务逻辑打包起来。我们使用时，不必关心内部是如何实现的。降低实现项目的难度
# 函数可以实现某一种功能。好处是减少重复代码，节省了代码的量，模块逻辑清晰。

def calculate_area(r):
    print('圆面积',3.14 * r * r)

calculate_area(3)  # 括号内输入半径

# 语法
## 函数定义：关键字def（define）函数名（参数）：语句块
## 参数：函数运行前需要告诉函数一些运行时需要的信息原料、数值，函数根据传入的参数，参与内部的逻辑运算。
## 函数调用：函数名（参数)

