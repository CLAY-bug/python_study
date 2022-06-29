# 作者 ： 赖鑫
# 2022年06月22日22时37分14秒
class Parent:
    x = 1


class Child1(Parent):
    pass


class Child2(Parent):
    pass


c1 = Child1()
c2 = Child2()
p = Parent()
print(c1.x, c2.x, p.x)
c1.x = 2
print(c1.x, c2.x, p.x)
p.x = 3
print(c1.x, c2.x, p.x)
