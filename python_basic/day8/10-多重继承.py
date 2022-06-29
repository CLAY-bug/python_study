# 作者: 王道 龙哥
# 2022年06月07日16时10分01秒
class A:
    def test(self):
        print('A test')

    def demo(self):
        print('A demo')


class B:
    def test(self):
        print('B test')

    def demo(self):
        print('B demo')

    def test2(self):
        print('B test2')

class C(A,B):
    def demo(self):
        print('C demo')

c=C()
print(C.__mro__)
c.demo()
c.test2()