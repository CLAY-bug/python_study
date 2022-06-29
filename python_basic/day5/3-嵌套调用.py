# 作者: 王道 龙哥
# 2022年06月04日10时15分52秒
def test1():
    print("*" * 50)
    print("test 1")
    print("*" * 50)


def test2():
    print("-" * 50)
    print("test 2")

    test1()

    print("-" * 50)


test2()