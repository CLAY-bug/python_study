# 作者: 王道 龙哥
# 2022年06月18日10时16分16秒
from multiprocessing import Process
import os
from time import sleep


def run_proc(name, age, **kwargs):
    for i in range(10):
        print('子进程运行中，name= %s,age=%d ,pid=%d...' % (name, age, os.getpid()))
        print(kwargs)
        sleep(0.2)


if __name__ == '__main__':
    p = Process(target=run_proc, args=('lele', 20), kwargs={'m': 3})
    p.start()
