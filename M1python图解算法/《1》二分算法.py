# 二分算法
list = [1, 3, 5, 6, 8, 9]
item = 5
guess = input('请输入猜测数字：')
def binary_search(list, item):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high)/2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid -1
            print('猜大了')
        else:
            low = mid +1
            print('猜小了')



