# 作者 ： 赖鑫
# 2022年06月12日18时24分44秒

class Dog:
    def __init__(self, name):
        self.name = name

    def game(self):
        print(f"{self.name}普通的玩耍！")


class XiaoTianQuan(Dog):
    def game(self):
        print(f"{self.name}到天上飞着玩！")


class Person:
    def __init__(self, name):
        self.name = name

    def game_with_dog(self, dog):
        print(f"{self.name}play with{dog.name} ")
        dog.game()


dog = Dog("小黄狗")
dog.game()
print('-'*50)
tian_dog = XiaoTianQuan("哮天犬")
tian_dog.game()
print('-'*50)
xiaoming = Person("小明")
xiaoming.game_with_dog(tian_dog)