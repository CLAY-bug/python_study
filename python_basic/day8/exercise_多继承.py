# 作者 ： 赖鑫
# 2022年06月12日18时09分38秒

class A:
    def test(self):
        pass

    def demo(self):
        print("我是A的demo")


class B:
    def test(self):
        pass

    def demo(self):
        print("我是B的demo")


class C(A, B):
    pass


c = C()
c.demo()
# 可以查看方法搜索顺序
# print(C.__mro__)
