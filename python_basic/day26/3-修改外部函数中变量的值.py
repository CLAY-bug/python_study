# 作者: 王道 龙哥
# 2022年06月28日16时24分00秒
x = 300


def test1():
    x = 200   #这个x是nonlocal的
    def test2():
        nonlocal x
        print("----1----x=%d" % x)
        x = 100  #一旦修改就必须加修饰
        print("----2----x=%d" % x)

    return test2

t=test1()  #拿到闭包的入口地址
t()  #运行闭包

#外部函数的形参也是nonlocal类型
def counter(start=0):
    def incr():
        nonlocal start
        start += 1
        return start
    return incr

c1 = counter(5)
print(c1())
print(c1())

c2 = counter(50)
print(c2())
print(c2())