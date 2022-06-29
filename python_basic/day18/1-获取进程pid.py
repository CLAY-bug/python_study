# 作者: 王道 龙哥
# 2022年06月18日09时54分55秒
from multiprocessing import Process
import os
import time


def run_proc():
    """子进程要执行的代码"""
    print('子进程运行中，pid=%d...' % os.getpid())  # os.getpid获取当前进程的进程号
    print('子进程将要结束...')
    while True:
        time.sleep(1)


if __name__ == '__main__':
    print('父进程pid: %d' % os.getpid())  # os.getpid获取当前进程的进程号
    p = Process(target=run_proc)
    p.start()
    print('父进程最后一句')
