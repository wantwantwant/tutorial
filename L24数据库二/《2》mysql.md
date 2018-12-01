mysql
===
## 介绍
流行的关系型数据库

## 安装
### 选择安装包
www.mysql.com / download(下载) / community（社区版） / mysql server(服务器)
打开下载页后 operating system（选择操作系统） 选microsoft windows （微软windows系统）
- msi microsoft windows installer 也就是.exe安装包。好处 有安装向导，自动添加环境变量，自动生成配置文件，自动注册windows服务。
- zip archive 也就是.zip压缩包。包含mysql主要文件，但跟windows结合部分环境变量、服务就需要手动建立。好处是版本最新，控制力强。
### 安装
1.新建文件夹C:/Program Files/MySQL   允许权限
2. .zip安装包解压☞刚才新建的文件夹，报解压错误，原因无权限。解决先解压到D盘，然后剪切至目录，弹窗时允许权限。

## 开启服务
介绍mysql工程的主要文件夹和文件作用。
- bin文件夹。可执行二进制程序。客户端mysql.exe，服务端mysql.exe，备份mysqldump.exe
- data。存放具体的数据
- my.ini。数据库服务启动时的默认配置文件，定义了mysqls目录，引擎，字符集，日志等关键信息，需要手动建立。

## 驱动

## 示例

## 