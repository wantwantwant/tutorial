# （了解) global 全球的
# (老写法，total是全局变量）从1加到100
# total = 0
# for i in range(1,101):
#     total = total + i
# print(total)

##global 显示声明变量为全局变量
total = 0
def add1():
    global total      # 全局的变量
    total = total + 1

add1()
add1()
add1()
print(total)

##（了解）nonlocal 非局部变量

# #def outer():
#     num = 10
#     def inner():
#         nonlocal num
#         num = 100
#         print(num)
#     inner()
#     print(num)
# outer()