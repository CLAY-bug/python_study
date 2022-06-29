# 作者: 王道 龙哥
# 2022年06月23日10时57分40秒
class Foo:
    """
    I am Foo doc
    """

    def __call__(self, *args, **kwargs):
        print('当对象加括号时，执行的是我')
        print(args)
        print(kwargs)


print(Foo.__doc__)
print('-' * 50)
obj = Foo()
obj('wangdao')

print('-' * 50)


class Province:
    country = '中国'

    def __init__(self, name, count):
        self.name = name
        self.count = count

    def func(self, *args):
        print('func')


print(Province.__dict__)  # 获取类的属性，即：类属性、方法
obj = Province('台湾', 3000)
print(obj.__dict__)  # 获取 对象obj 的属性

print('-' * 50)
print('对象使用[]的操作实现，不重要')


class Foo(object):

    def __getitem__(self, key):
        print('__getitem__', key)

    def __setitem__(self, key, value):
        print('__setitem__', key, value)

    def __delitem__(self, key):
        print('__delitem__', key)


obj = Foo()

result = obj['k1']  # 自动触发执行 __getitem__
obj['k2'] = 'laowang'  # 自动触发执行 __setitem__
del obj['k1']  # 自动触发执行 __delitem__
