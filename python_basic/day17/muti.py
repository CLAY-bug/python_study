# 作者 ： 赖鑫
# 2022年06月19日21时50分02秒
import os
from multiprocessing import Process
from time import sleep


def son_process():
    print(f"i am son process:{os.getpid()}")


if __name__ == '__main__':
    p = Process(target=son_process)
    p.start()
    sleep(1)
    print(f'i am father process:{os.getpid()}')
