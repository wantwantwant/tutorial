from L8包.package.pack1.py1 import * # 绝对路径
from . import py1      #相对路径 同级目录
from .. import pack1   # 父级目录  py2.py在pack1目录下，pack1的目录下是package包目录下，所以可以引用package包下的内容。
from .. pack1 import py1