# 1.用户随意输入一些字符串，判断字符串中字母数字，空格，其他各有多少个
alpha_num = 0
digit_num = 0
space_num = 0
other_num = 0

user_input = input('随意输入一些东西：')

for i in user_input:
    if i.isalpha():
        alpha_num += 1
    elif i.isdigit():
        digit_num += 1
    elif i.isspace():
        space_num += 1
    else:
        other_num += 1

print('字母{}，数字{}，空格{}，其他{}'.format(alpha_num,digit_num,space_num,other_num))