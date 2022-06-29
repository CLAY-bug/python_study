# 作者 ： 赖鑫
# 2022年06月22日20时27分53秒
class Person:
    """人类"""

    def sleep(self):
        pass

    def eat(self):
        print("我每顿要吃3顿饭")

    def run(self):
        pass


class Man(Person):
    """男人"""

    def sleep(self):
        print('我每天需要睡6个小时')

    def run(self):
        print("我能跑10公里")


class Woman(Person):
    """女人"""

    def sleep(self):
        print("我每天需要睡7个小时")

    def run(self):
        print("我能跑3公里")


class Child(Person):
    def sleep(self):
        print("我们天需要睡8个小时")

    def run(self):
        print("我能跑2公里")


class Factory:
    """
    工厂模式：在创建对象时不对外暴露创建逻辑，直接返回类对象
    """

    def create_object(self, name):
        if name == "man":
            return Man()
        elif name == "woman":
            return Woman()
        elif name == "chile":
            return Child()
        else:
            return Person()


factory = Factory()
people = factory.create_object('man')
people.run()
people.sleep()
people.eat()
