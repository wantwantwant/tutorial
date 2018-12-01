# 作业一：类初识
"""
1.写一个“人类”类。
  类有以下属性：
  -姓名
  -人种（黄种人，白种人，黑种人）
  -国家（中国 美国 韩国）
  -身高（180 160）
  -体重（70）
  方法、功能：
  -打印基本信息
  -（选座)打印BMI指数 体重kg/身高m的平方
"""

class People():
    def __init__(self,name,race,country,height,weight):
        self.name=name
        self.race=race
        self.country=country
        self.height=height
        self.weight=weight

    def print_race(self):
        print('{}的肤色种类是{}'.format(self.name,self.race))

    def print_country(self):
        print('{}的国家是{}'.format(self.name,self.country))

    def print_height(self):
        print('{}的身高是{}'.format(self.name,self.height))

    def print_weight(self):
        print('{}的体重是{}'.format(self.name,self.weight))

    def print_info_(self):
        print('我叫{}，我是{}，我来自{}，身高{}，体重{}'.format(
            self.name,self.race,self.country,self.height,self.weight
        ))

peo1=People('夏明','黄种人','中国',180,70)
peo2=People('尚','白种人','韩国',160,70)
peo3=People('Mary','黑种人','美国',160,70)

peo1.print_info_()
peo2.print_info_()
peo3.print_info_()
