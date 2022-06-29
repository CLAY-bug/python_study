# 作者 ： 赖鑫
# 2022年06月29日16时32分36秒
import time


def get_time(func):
    def set_func():
        start = time.time()
        func()
        end = time.time()
        print(f'time = {end - start}')

    return set_func


@get_time
def test():
    print("这个函数的运行时间为：")


test()
