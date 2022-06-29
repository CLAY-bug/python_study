# 作者 ： 赖鑫
# 2022年06月23日10时45分48秒
class Foo:
    def get_bar(self):
        print('getter...')
        return 'laowang'

    def set_bar(self, value):
        print("setter...")
        return 'value=' + value

    def del_bar(self):
        print('deleter...')
        return 'laowang'

    BAR = property(get_bar, set_bar)


f = Foo()
print(f.BAR)
