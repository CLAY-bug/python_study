# 作者 ： 赖鑫
# 2022年06月29日16时39分50秒

import time


def time_fun(func):
    def warped_func():
        print(f'{func.__name__} called at {time.ctime()}')
        func()

    return warped_func


# @time_fun

def foo():
    print('i am foo')


foo = time_fun(foo)

foo()
time.sleep(2)
foo()
