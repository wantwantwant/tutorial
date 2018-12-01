# 用户输入(result 成绩)
res = input('请输入成绩')
res = float(res)

# 判断
if res < 0 or res > 100:
    print('用户输入不合法')
if 0 <= res < 60:
    print('不及格')
elif 60 <= res <= 100:
    print('及格')
if 60 <= res < 70:
    print('D')
elif 70 <= res < 80:
    print('C')
elif 80 <= res < 90:
    print('B')
elif 90 <= res <= 100:
    print('A')