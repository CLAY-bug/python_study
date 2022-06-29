# 作者 ： 赖鑫
# 2022年06月12日11时14分35秒

class Animal:
    """动物类"""

    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} can eat")

    def drink(self):
        print(f"{self.name} can drink")

    def run(self):
        print(f"{self.name} can run")

    def sleep(self):
        print(f"{self.name} want sleep")


class Dog(Animal):
    """狗类"""

    def bark(self):
        print(f"{self.name} can bark")


class Cat(Animal):
    """猫类"""

    def catch(self):
        print(f"{self.name} can catch")


class XiaoTainQuan(Dog):
    def bark(self):
        print("我要像神一样叫")
        super().bark()


# 创建狗的实例
dog = Dog("小黄狗")
dog.run()
# 创建猫的实例
cat = Cat("小黑猫")
cat.sleep()
# 创建哮天犬的实例
tian = XiaoTainQuan("哮天犬")
tian.bark()
