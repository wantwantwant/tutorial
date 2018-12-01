# if练习

#计算BMI指数

# 用户输入
height = input('请输入身高(cm)')
weight = input('请输入体重（kg)')
height = float(height)
weight = float(weight)

# 计算bmi
bmi = weight / (height/100 * height/100)
print(bmi)

# if判断
if bmi < 18.5:
    print('体重偏轻')
elif 18.5 <= bmi < 23.9:
    print('正常')
elif 23.9 <= bmi <32:
    print('偏重')
elif bmi >= 32:
    print('超重')


# 用户输入(result 成绩)
res = input('请输入成绩')
res = float(res)

# 判断
if 0 <= res < 60:
    print('不及格')
elif 60 <= res <= 100:
    print('及格')








