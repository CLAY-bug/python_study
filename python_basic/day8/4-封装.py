# 作者: 王道 龙哥
# 2022年06月07日14时35分37秒
class Person:
    """人类"""

    def __init__(self, name, weight):

        self.name = name
        self.weight = weight

    def __str__(self):

        return "我的名字叫 %s 体重 %.2f 公斤" % (self.name, self.weight)

    def run(self):
        """跑步"""

        print("%s 爱跑步，跑步锻炼身体" % self.name)
        self.weight -= 0.5

    def eat(self):
        """吃东西"""

        print("%s 是吃货，吃完这顿再减肥" % self.name)
        self.weight += 1


xiaoming = Person("小明", 75)
print(xiaoming)
xiaoming.run()
xiaoming.eat()
xiaoming.eat()
print(xiaoming)
# 小美爱跑步
xiaomei = Person("小美", 45)

xiaomei.eat()
xiaomei.run()
print(xiaomei)

