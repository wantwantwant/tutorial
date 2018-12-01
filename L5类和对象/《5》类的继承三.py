# 继承 > 重写
# 引题1：比如说一个计算机系有 电商方向、软件方向，他们的课程70%一样
#   （数学英语C语言）其他30%不一样（电商seo优化、软件方向xx编程框架）。
#    而上节课例子run方法是子类完全重写覆盖父类方法。
# 引题2：类的继承第一节中的学生、老师类例子用继承方式写出来

class People(object):
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex

    def say_hi(self):
        print('hello')

    def work(self,time):
        if time < 8:
            print('正常上班')
        elif time > 8:
            print('加班时间')

class Student(People):
    def __init__(self,name,age,sex,hobby,parent_phone):
        #self.name=name
        # self.age=age
        # self.sex=sex
        # self.hobby=hobby
        # self.parent_phone=parent_phone
        super()

    def work(self,time):
        print('学生不需要工作')

class Teather(People):
    def __init__(self,name,age,sex,salary,class_num):
        # 1>一个一个属性写构造函数
        # self.name=name
        # self.age=age
        # self.sex=sex
        # 2>类名。方法名
        # People.__init__(name,age,sex)
        # 3> super()
        super(Teather,self).__init__(name,age,sex)
        # 4> 省略参数的super()
        super().__init__(name,age,sex)
        self.salary=salary
        self.class_num=class_num




stu1=Student('小明',10,'male','game','13722133322')
stu1.say_hi()
stu1.work(time=8)
tea1=Teather('杨老师',27,'male',10000,314)
tea1.say_hi()

"""
完全重写：子类重写父类方法，完全覆盖父类方法内容。像上一节例子，
Cat类的run（）方法完全替代了父类Animal类中的run（）的内容。

部分重写:子类重写父类方法，继承父类方法中一部分内容，又有个性化部分。

super():调用父类。重用父类属性、方法，减少了代码量。专为继承设计。
子类调用完父类相同之处后，个性化的东西可以另外写。
语法：原始语法super（子类名，子类实例），省略参数super（）py2不支持。
优点：方便调用父类中的东西；代码复用；父类名变化时子类不用过多修改，好维护。

"""
