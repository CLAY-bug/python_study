# 作者: 王道 龙哥
# 2022年06月23日10时51分04秒
class Foo:

    def get_bar(self):
        return 'laowang'

    def set_bar(self, value):
        print(value)

    def del_bar(self):
        print('del_bar')

    Bar = property(get_bar, set_bar, del_bar, 'I am Bar 的注释')


obj = Foo()
obj.Bar
obj.Bar = 200
print(Foo.Bar.__doc__)  # 这里一定要用类名
del obj.Bar
