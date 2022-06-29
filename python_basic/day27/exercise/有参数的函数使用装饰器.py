# 作者 ： 赖鑫
# 2022年06月29日16时48分25秒

def set_func(func):
    def warpped_func(a):
        print(f'my name is {func.__name__}')
        print(a)
        func(a)

    return warpped_func


@set_func
def foo(a):
    print(hex(a))


foo(12)
