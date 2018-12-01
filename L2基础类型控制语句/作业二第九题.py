# 第九题

for x in range(1,10):
    for y in range(0,10):
        for z in range(0,10):
            num = x*100 + y*10 + z
            if x**3 + y**3 + z**3 ==num:
                print(num)




