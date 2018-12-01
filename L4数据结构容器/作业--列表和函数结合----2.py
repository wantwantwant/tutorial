## 检查获取传入列表对象的所有奇数位索引（下标为1,3,5）
# 对应的元素，并将其作为新列表返回给调用者，打印新列表内容。
# #list1 = 0
# for num in range(1,10,2):
#      print(num)
#      num = list1
# for i in range(1,10):
#     list1.append(i)
# print(list1)
#
#


# list1 = input(1,10)
# def num_list1():
#      print(num_list1(1,10,2))

stu_list = ['小周','小吴','小郑','小王','小李']
new_list= []

def fn2(stu_list):
    for i in range(0,len(stu_list)):
        if i % 2 ==1:        # 奇数
            print(stu_list[i])
            new_list.append(stu_list[i])
        return new_list

print(fn2(stu_list))