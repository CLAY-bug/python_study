# 作者 ： 赖鑫
# 2022年06月18日13时01分19秒

from multiprocessing import Process
from time import sleep
import os


def son_processing(name, age, **kwargs):
    for i in range(10):
        print(f'{i}:子进程的名字:{name}, 年龄:{age}, pid为：{os.getpid()}')
        print(kwargs)


if __name__ == '__main__':
    p = Process(target=son_processing, args=('小明', 18), kwargs={'小红': 20})
    p.start()
    sleep(1)
    p.terminate()
