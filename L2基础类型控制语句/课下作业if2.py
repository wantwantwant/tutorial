# 公里数输入（km）
km = input('请输入公里数:')
km = float(km)

pay = 0   # 给pay一个初始值

# 计算费用（pay = （费用)）
# pay = 8 + 1.2 *(12-2) + 1.5 * (20-12)
if km <= 2:
    pay = 8
if 2 < km <= 12:
    pay = 8 + 1.2*(km-2)
if 12 < km :
    pay =  8 + 1.2 * (12-2) + 1.5 * (km-12)

print(pay)




## 已知两个数，比大小

a = int(input('输入第一个数：'))
b = int(input('输入第二个数：'))

if a < b:
    print('第二个数大')
elif a > b:
    print('第二个数大')
else:
    print('两个数一样大')



