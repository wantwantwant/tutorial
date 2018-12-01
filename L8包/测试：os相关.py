import os, os.path, re

# path = ('D:\E')
#
# # 父目录，文件夹名字，文件名字
# for parent, dirnames, filenames in os.walk(path):
#     print(dirnames, filenames)
#     os.remove('D:\E\E\wegame\lol\lol.exe')
#     print('删除成功')


test = 'D:\E\E\wegame\lol'

import os, shutil
if __name__=='__main__':
    for parent, dirnames, filenames in os.walk(test,  followlinks=True):
        for filename in filenames:
            file_path = os.path.join(parent, filename)
            print('文件名：%s' % filename)
            print('文件完整路径：%s\n' % file_path)


delList = []
delList = os.listdir(test )
for f in delList:
     E = os.path.join( test, f )  #获得脚本的绝对路径
if os.path.isfile(E):           #列出指定文件夹下的文件并删除
    os.remove(E)
print(E + " was removed!")
if os.path.isdir(E):
    shutil.rmtree(E,True)     #rmtree删除文件目录及其内容
    os.remove('D:/E/wegame/lol/lol.exe')
print ("Directory: " + E +" was removed!")

