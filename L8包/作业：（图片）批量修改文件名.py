import os
path = ('C:/img')

f = os.listdir(path)

n = 0
for files in f:
    oldname = os.path.join(path,files)
    filename = os.path.splitext(files)[0]
    filetype = os.path.splitext(files)[1]
    newname = os.path.join( path+str(n+1) + filetype)
    os.rename(oldname,newname)
    n += 1

# import os
# import os.path
# n = os.listdir('')
# os.chdir('')
# b = 1
# for i in n:
#     filename ="图片"+str(1)+".jpg"
#     os.rename(i,filename)
#     b = b+1

