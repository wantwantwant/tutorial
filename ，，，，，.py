#通过循环遍历
import os, shutil
if __name__=='__main__':
    work_dir = 'D:\E\E\wegame\lol'
    for parent, dirnames, filenames in os.walk(work_dir,  followlinks=True):
        for filename in filenames:
            file_path = os.path.join(parent, filename)
            print('文件名：%s' % filename)
            print('文件完整路径：%s\n' % file_path)


