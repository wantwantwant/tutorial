# 第八题
total = 0
for x in range(1,10):
    for y in range(0,10):
        for z in range(0,10):
            print(x,y,z,y,x)
            hui = x*10000 + y*1000 + z*100 + y*10 + x
            total += hui
print(total)


total = 0
for i in range(10000,99999+1):
    b5 =i // 10000
    b4 =(i - b5*10000) // 1000
    b3 =(i - b5*10000 - b4*1000) // 100
    b2 =(i - b5*10000 - b4*1000 - b3*100) // 10
    b1 =(i - b5*10000 - b4*1000 - b3*100 - b2*10)
    if b5 == b1 and b4 == b2:
        total += 1
        print(i)
print(total)

