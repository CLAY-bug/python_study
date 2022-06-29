# 作者 ： 赖鑫
# 2022年06月28日22时00分29秒

def add_first(func):
    print("start 1")

    def call_func(*args, **kwargs):
        print('第一次验证')
        return func(*args, **kwargs)

    return call_func


def add_second(func):
    print("start 2")

    def call_func(*args, **kwargs):
        print("第二次验证")
        return func(*args, **kwargs)

    return call_func


# 就近原则，由下向上进行装饰
# 执行的时候由上向下开始执行
@add_first
@add_second
def test():
    print('我有多个装饰器')


test()
