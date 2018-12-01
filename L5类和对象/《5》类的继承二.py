# 类的继承和重写
# 引题：上节课例子展示了子类继承父类，子类可以继承父类的属性和方法。
#  但是生活中往往子类除了具备一些父类的特征，还具备自己个性化的特征。
#   例如父类手机类，子类OPPO手机类 独特特征拍照，苹果手机类 系统好。

class Animal(object):
    def __init__(self,name):
        self.name=name

    def run(self):
        print('动物在跑')

class Dog(Animal):
    def swim(self):
        print('狗会游泳')

class Cat(Animal):
    def crawl_tree(self):
        print('猫会爬树')

    def run(self):
        print('猫灵活地跑')


dog1=Dog('阿黄')
dog1.run()
dog1.swim()
cat1=Cat('小花')
cat1.run()
cat1.crawl_tree()

"""
子类个性化：只要在子类当中书写个性化属性和方法。

重写：比如一个父类下有二十个子类，这些动物都有run方法，所以公共
run方法应该写在Animal类中，但是个别子类run姿势奇特想个性化定义，
那么在子类中实现run方法。
子类和父类中出现同名方法，叫做重写。子类中的方法覆盖父类中同名
方法，子类方法生效。

"""
# 重写和重载的区别