# 作者 ： 赖鑫
# 2022年06月28日21时30分34秒

def set_func(func):
    def call_func():
        print("1----")
        print("2----")
        func()

    return call_func


@set_func
def test1():
    print('---test1---')


test1()
