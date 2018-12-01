# pip
"""
# pip：python install package,python第三方包管理工具。安装Python解释器时已自带。目录已添加到环境变量中。
# 包管理工具：包是别人写好的代码。经常有这种情况，比如爬虫框架功能的A包，里面引用了负责解析网页的B包，B包引用了更加基础底层的C包。包关系成树状引用。B包依赖C包。直接使用A包，运行报错缺少B包，缺少依赖包。
# 为了解决依赖包问题，包管理工具出现，主要功能：管理、下载、上传包。解决依赖，安装一个包时会把相关的依赖包都安装好。


 pypi：https://pypi.org/ 是查找、安装、发布Python包的一个平台,pip工具默认从pypi下载包。
"""

"""
pip list   # 输出安装过的三方包的列表。
pip search 关键字  # 搜索包含关键字的包名。
pip install 包名   #（常用）安装包的本质是从pypi下载，解压复制到C:\Python36\Lib\site-packages 下。默认安装包的最新版本。
pip install requests==2.19.0
pip uninstall 包名  # 卸载包
"""

"""
批量备份和安装：
pip freeze > requirement.txt  # 讲解释器中的包和版本导出到一个文件中。
pip install requirement.txt #根据requirement.txt的信息批量安装对应版本的包。
"""

"""
pip安装速度慢的问题：
 因为服务器在国外，为了改善这个问题，国内一些厂商或大学做了pypi网站的镜像。
国内的镜像站豆瓣源、网易源。
常用国内源：
豆瓣：http://pypi.douban.com/simple/ 
清华：https://pypi.tuna.tsinghua.edu.cn/simple

临时：pip install -i https://pypi.tuna.tsinghua.edu.cn/simple/ pillow
永久修改（推荐）：C:/User/用户名 下，新建pip文件夹，新建文本文档pip.ini：[global]
index-url = https://pypi.douban.com/simple/
"""


"""
可能出现的错误：
1.红字错误。 没有合适系统的安装包，跟C C++相关的库。
2.拒绝访问。权限问题，使用管理员权限的终端运行。
以下不影响：
1.最后黄字警告。pip版本升级提示，可以忽略。
2.黄字警告。pip所在的目录没有添加的环境变量中。
3.requirement already satisfied .之前已经成功安装过此包了。
4.cache 缓存。之前已经下载过安装包，再次安装时不会再从网上下载。
"""