# 作者: 王道 龙哥
# 2022年06月28日16时54分46秒
def add_first(func):
    print("---开始进行装饰权限1的功能---")

    def call_func(*args, **kwargs):
        print("---这是权限验证1----")
        return func(*args, **kwargs)

    return call_func


def add_second(func):
    print("---开始进行装饰权限2的功能---")

    def call_func(*args, **kwargs):
        print("---这是权限验证2----")
        return func(*args, **kwargs)

    return call_func


@add_first
@add_second
def test1():
    print('--test1--')


# 离的近的先装饰，离的远的后装饰
# 先装饰的后执行
test1()
