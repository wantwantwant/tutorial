# 写文本文件

# 回忆读取文本文件示例
# file = open (file='chinese_utf-8.txt',mode='r',encoding='utf-8')
# content = file.read()
# print(content)
# file.close()



# 写文件
file = open('write.txt','w',encoding='utf-8')
file.write('hello world')
file.write('小明')
file.write('\n')
file.write('天黑的开始早了')

file.writelines(['第一行','second line','第三行'])





"""
写入文件  open函数先打开一个空文本文件。
模式为'w',意为write写。文件名如果不存在，执行代码时系统会自动生成一个文件。
utf-8 UTF-8 utf8 utf_8 这些写法都行。同理ascii ASCII  gbk GBK都可以。

"""
