# 作者: 王道 龙哥
# 2022年06月23日09时49分47秒
class Foo:
    def func(self):
        print('I am func')

    @property  # @是装饰
    def prop(self):
        print('I am prop')


f = Foo()
f.func()
f.prop  # 这是一个property属性
print('-' * 50)


class Goods:
    @property
    def size(self):
        return 100


desk = Goods()
width = desk.size
print(width)
