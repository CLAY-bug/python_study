# 作者 ： 赖鑫
# 2022年06月29日09时14分35秒

import time


def set_func(func):
    def call_func():
        start_time = time.time()
        func()
        stop_time = time.time()
        print(f'time= {stop_time - start_time}')

    return call_func


@set_func
def test1():
    print('-----test1')
    for i in range(10000):
        pass


test1()
