# 作者 ： 赖鑫
# 2022年06月29日17时05分24秒

def set_func(func):
    def warpped_func(*args, **kwargs):  # 无论函数有多少个参数都能接收
        print('---start---')
        func(*args, **kwargs)  # 进行参数拆包
        print("---end---")

    return warpped_func


@set_func
def foo(num, *args, **kwargs):
    print(f'num = {num}')
    print(f'args = {args}')
    print(f'kwargs = {kwargs}')


foo(1)
foo(4, 5, 6)
foo(7, 8, 9, k=100)
