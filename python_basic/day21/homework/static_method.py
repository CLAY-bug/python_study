# 作者 ： 赖鑫
# 2022年06月22日22时54分07秒

class Foo:
    def __init__(self, name):
        self.name = name

    def orf_func(self):
        """定义实例方法，至少有一个self参数"""
        print(self.name)
        print('这是实例方法')

    @classmethod
    def class_func(cls):
        """定义一个类方法，至少有一个cls参数"""
        print('这是类方法')

    @staticmethod
    def static_func():
        """
        静态方法：主要用来存放逻辑性的代码
        不会涉及到类的属性和方法
        :return:
        """
        print('这是一个静态方法')


f = Foo('China')
f.orf_func()  # 实例方法通过对象名来调用
Foo.class_func()  # 类方法通过类名直接调用
Foo.static_func()  # 调用静态方法
