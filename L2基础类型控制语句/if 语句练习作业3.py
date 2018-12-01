# 已知三个数，比大小。

#a = int(input('请输入第一个数：'))
#b = int(input('请输入第二个数：'))
#c = int(input('请输入第三个数：'))

# #max_num = a      # 存储最大值，max_num就好像老大一样，谁比他强，谁就是最大者，比较完谁最强就是老大

# #if a >b and a >c:
#     print('第一个数最大')
# #elif b >a and b >c:
#     print('第二个数最大')
# elif c >a and c >b:
#     print('第三个数最大')
#


# if a > b > c:
#     print('第一个数最大')
# elif b > c > a:
#     print('第二个数最大')
# elif c > b >a:
#     print('第三个数最大')
# elif c > a > c:
#     print('第三个数最大')
#
#


def three_number():
    a = int(input('请输入第一个数：'))
    b = int(input('请输入第二个数：'))
    c = int(input('请输入第三个数：'))
    result = a
    if b > a:
        result = b
    elif c > a:
        result = c
    else:
        result = a
    return result

print('最大值',three_number())

