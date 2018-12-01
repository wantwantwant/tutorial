# 私有属性

# 1 引题
class Student():
    def __init__(self,name,score,sex):
        self.name=name
        self.score=score
        self.sex=sex

    def print_score(self):
        print('{}的成绩是{}'.format(self.name,self.score))

    def print_sex(self):
        print('{}的性别是{}'.format(self.name,self.sex))
# 实例化
stu1=Student('小明',90,'男')
stu2=Student('小红',100,'女')
# 调用对象属性
print(stu1.name)
print(stu1.score)
print(stu2.name)
print(stu2.score)
# 写属性
stu1.score=100
print(stu1.score)

# 上面的例子说明类的属性可以读也可以被修改，但是这样会导致安全问题。
#  类内部保密只需要暴露跟外部通信的接口，外部不应该直接修改类的属性。

# 2.私有属性
class Student2():
    def __init__(self,name,score,sex):
        self.__name=name
        self.__score=score
        self.__sex=sex

stu1 = Student2('小明', 90, '男')
print(stu1.score)
# 双下划线开头的属性不能直接访问，这样确保了安全性。
# 但是有的时候我们又想获得对象的信息。

# 3. getter和setter函数
class Student3():
    def __init__(self, name, score, sex,password):
        self.__name = name
        self.__score = score
        self.__sex = sex
        self.__password=password

    def get_score(self):
        return self.__score

    def set_score(self,score):
        if score<0 or score>100:
            raise ValueError('分数输入错误')
        self.__score=score

stu1 = Student3('小明', 90, '男','1234d5')
print(stu1.get_score())
stu1.set_score(100)
print(stu1.get_score())

#stu1.__score=100   # 私有属性不能被直接修改
#print(stu1.get_score())
# java中类每个属性都有getter setter方法。
# getter和setter函数可以提供更加精确的控制。

# 4.（了解）property装饰器
# 因为上面的getter setter函数写起来比较麻烦，所以Python提供了属性装饰器。
class Student4():
    def __init__(self, name, score, sex,password):
        self.__name = name
        self.__score = score
        self.__sex = sex
        self.__password=password
    @property      #getter_score
    def get_score(self):
        return self._score
    @score.setter      #setter_score
    def set_score(self,score):
        if score<0 or score>100:
            raise ValueError('分数输入错误')
        self.__score=score

stu1 = Student4('小明', 90, '男','1234d5')
print(stu1.score)
stu1.score=98
print(stu1.score)