# 作者 ： 赖鑫
# 2022年06月28日20时56分37秒

x = 300


def test1():
    x = 200

    def test2():
        nonlocal x  # 使用外部变量的时候需要使用关键字nonlocal
        print(f"1----x = {x}")
        x = 100
        print(f"2----x = {x}")

    return test2


t1 = test1()  # 返回的是test2，即t1是test2函数的引用
t1()  # 与test2()函数作用相同
