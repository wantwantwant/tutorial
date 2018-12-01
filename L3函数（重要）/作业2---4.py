# 输出斐波拉切数列（1, 1, 2, 3, 5, 8, 13, 21, ...）


print('1、','1、',end='')
def fibs(num):
    print





def fibs(num):
    result = [0, 1]
    for i in range(2, num):
        result.append(result[-2] + result[-1])
    return result


print(fibs(9))



def fibs(num):
    if num == 1:
        return 1
    else:
        return fibs(num - 1) + fibs(num - 2)


for i in range(10):
    print (fibs(i))

