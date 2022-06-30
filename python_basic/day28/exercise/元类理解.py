# 作者 ： 赖鑫
# 2022年06月30日19时28分29秒
Foo = type('Foo', (), {'good': True})  # 使用type创建类提供类属性


def test(self):
    print(f'元类实例方法:{self.good}')


@staticmethod
def test_static():
    print(f'元类静态方法')


@classmethod
def test_cls(cls):
    print(f'元类类方法{cls.good}')


# 通过type创建类并添加各种方法，继承父类
FooChild = type('FooChild', (Foo,), {'test': test, 'test_static': test_static, 'test_cls': test_cls})
foochild = FooChild()
foochild.test()  # 调用实例方法
FooChild.test_static()  # 调用静态方法
FooChild.test_cls()  # 调用类方法
