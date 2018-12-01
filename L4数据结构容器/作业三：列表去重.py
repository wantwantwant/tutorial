# 列表去重  不用set

a=[1,2,3,4,5,1,3]
new_list=[]
for i in a:
    if i not in new_list:
        new_list.append(i)
print(new_list)



