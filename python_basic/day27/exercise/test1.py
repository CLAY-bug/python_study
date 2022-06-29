# 作者 ： 赖鑫
# 2022年06月29日19时33分32秒

def set_func(func):
    def call_func(*args, **kwargs):
        level = args[0]
        if level == 1:
            print("---1---")
        elif level == 2:
            print("---2---")
        return func()

    return call_func


@set_func
def test1():
    print("---test1---")
    return "ok"


@set_func
def test2():
    print("---test2---")
    return "ok"


a = test1(1)
print(a)
