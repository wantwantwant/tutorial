# д�ı��ļ�

# �����ȡ�ı��ļ�ʾ��
# file = open (file='chinese_utf-8.txt',mode='r',encoding='utf-8')
# content = file.read()
# print(content)
# file.close()



# д�ļ�
file = open('write.txt','w',encoding='utf-8')
file.write('hello world')
file.write('С��')
file.write('\n')
file.write('��ڵĿ�ʼ����')

file.writelines(['��һ��','second line','������'])





"""
д���ļ�  open�����ȴ�һ�����ı��ļ���
ģʽΪ'w',��Ϊwriteд���ļ�����������ڣ�ִ�д���ʱϵͳ���Զ�����һ���ļ���
utf-8 UTF-8 utf8 utf_8 ��Щд�����С�ͬ��ascii ASCII  gbk GBK�����ԡ�

"""
