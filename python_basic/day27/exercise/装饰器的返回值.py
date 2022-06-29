# 作者 ： 赖鑫
# 2022年06月29日17时16分01秒


def time_func(func):
    def wrapped():
        print(f'my name is {func.__name__}')
        # 当函数中有返回值的时候，必须在在闭包中增加返回，不然取到None
        return func()

    return wrapped


@time_func
def foo():
    return '我是函数'


print(foo())
