## 判断用户传入的列表的长度是否大于5.小于5返回none。大于等于5的
##返回前两个长度的内容。

# #while True:
#     s = input('随便输入点什么:')
#
#     if len(s) < 5:
#         print (None)
#     elif len(s) >= 5:
#         print(s[0:2])

s = input('随便输入点什么：')
def _len_(s):
    return('长度')
    print(len(s))

if len(s) < 5:
       print (None)
elif len(s) >= 5:
     print(s[0:2])


def fn1(stu_list):
    if len(stu_list) < 5:
        return None
    elif len(stu_list) >=5:
        return stu_list[:2]

