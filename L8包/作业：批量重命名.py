
import os
import os.path
import re

path = ('C:/test')

# 三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
i=0
for parent, dirnames, filenames in os.walk(path):
    print(filenames)
    for filename in filenames:
        i =i+1
        o_name=os.path.join(path,filename)
        filename = os.path.splitext(filename)[0]  # 文件名
        filetype = os.path.splitext(filename)[1]  # 文件扩展名
        n_name = os.path.join(path, str(i) + filetype)  # 新的文件路径
        os.rename(o_name,n_name)  # 重命名
