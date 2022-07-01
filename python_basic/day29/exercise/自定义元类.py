# 作者 ： 赖鑫
# 2022年07月01日13时04分14秒

# 自定义元类需要继承type
class UpperAttr(type):
    # 重写__new__方法，参数与type是一样的
    def __new__(cls, class_name, class_parent, attrs):
        new_attr = {}  # 把符合条件的属性都放进新的字典
        for name, value in attrs.items():
            if not name.startswith('__'):
                new_attr[name.upper()] = value
        return type.__new__(cls, class_name, class_parent, new_attr)


class Animal(metaclass=UpperAttr):
    """
    利用metaclass参数生成类，用来限制类的生成
    """
    food = 'meat'

    def hello(self):
        print('hello')


class ChildAnimal(Animal):
    """
    继承Animal
    """
    pass


# 实例化子类
dog = ChildAnimal()
# 子类可以调用父类的属性和方法
dog.HELLO()
print(ChildAnimal.FOOD)
