# 类变量和静态方法练习

class Robot():
    population=0

    def __init__(self,name):
        self.name=name
        Robot.population+=1

    def say_hi(self):
        print('大家好，我是{}'.format(self.name))

     #1 类方法装饰器
    @classmethod
    def how_many(cls):
         print('机器人总人数：{}',cls.population)

     # 2 静态方法装饰器
    #@staticmethod
    #def how_many():
    #    print('目前总人口',Robot.population)

   # 3 对象方法
   # def how_many(self):
   #    print('目前总人口',Robot.population)

    def die(self):
        Robot.population-=1
        print(Robot.population)

robot1=Robot('XR-01')
robot1.say_hi()
Robot.how_many()
robot2=Robot('XR-02')
Robot.how_many()
robot2.die()
Robot.how_many()



