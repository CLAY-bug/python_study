# 作者 ： 赖鑫
# 2022年06月22日20时23分27秒

class Animal():
    def eat(self):
        pass

    def voice(self):
        pass


class Dog(Animal):
    def eat(self):
        print("狗吃骨头")

    def voice(self):
        print("狗汪汪叫")


class Cat(Animal):
    def eat(self):
        print("猫吃鱼")

    def voice(self):
        print('猫喵喵')


class Factory():
    """工厂"""

    def create_animal(self, animal_name):
        if animal_name == 'dog':
            return Dog()
        if animal_name == 'cat':
            return Cat()


f = Factory()
animal = f.create_animal('dog')
animal.eat()
