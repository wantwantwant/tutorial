# 循环中断之continue

while True:
    s = input('随便输入点什么：')

    if len(s) < 3:
        print('太短了，请输入三个字以上字符的内容。')
        continue

    print('你输入的内容是：{}，长度是{}'.format(s,len(s)))

# continue:中断一次循环，并没有中断整个循环，下次循环正常运行。
# 场景：清洗数据