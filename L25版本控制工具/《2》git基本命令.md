git基本命令
===
打开git bash或cmd终端，cd到项目文件夹根目录下。cd/pycharmProjects/testgit
- git init。初始化本地仓库git，会看到项目文件夹生成.git隐藏文件夹，这个文件夹会记录以后的每次更改和提交。
- git add 文件名。跟踪一个文件。git add 1.py
- git add . 。跟踪当前文件夹所有文件。
 - git init。初始化本地仓库git，会看到项目文件夹下生成，
- git隐藏文件夹生成，这个文件夹会记录以后每次的更改和提交。
-git config --global user.email "你的邮箱"
-git config --global user.name "你的姓名"


- git add 文件名。跟踪一个文件。git add 1.py
- git add .   。跟踪当前文件夹所有文件。
- git merge 副分支。合并副分支内容到当前分支。

###分支
（*newfeature） git add 。 git commit -m “”
（*newfeature） git checkout master
（*newfeature） git merge newfeatrue 这样就会把新分支的修改分支的修改合并到主分支下。 
###撤回

##还原
git log 查看提交记录，记忆想要还原的id值。
git reset --hard 提交记录的id 还原
