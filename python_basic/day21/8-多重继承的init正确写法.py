# 作者: 王道 龙哥
# 2022年06月22日11时37分27秒
class Parent:
    def __init__(self, name, *args, **kwargs):  # 多重继承一般会使用多值参数，来接收不定数量的参数
        print('parent的init开始被调用')
        self.name = name
        print('parent的init结束被调用')


class Son1(Parent):
    def __init__(self, name, age, *args, **kwargs):
        print('Son1的init开始被调用')
        self.age = age
        super().__init__(name, *args, **kwargs)
        print('Son1的init结束被调用')


class Son2(Parent):
    def __init__(self, name, gender, *args, **kwargs):
        print('Son2的init开始被调用')
        self.gender = gender
        super().__init__(name, *args, **kwargs)
        print('Son2的init结束被调用')


class Grandson(Son1, Son2):
    def __init__(self, name, age, gender):
        print('Grandson的init开始被调用')
        super().__init__(name, age, gender)  # 调用父类的方法只能用super()，不能直接用变量名调用
        print('Grandson的init结束被调用')


print(f'多重继承按照这个顺序调用:{Grandson.mro()}')
grandson = Grandson('grandson', 12, '男')
