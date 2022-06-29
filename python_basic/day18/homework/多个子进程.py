# 作者 ： 赖鑫
# 2022年06月18日17时03分59秒

from multiprocessing import Queue, Process
import os
from time import sleep


def write_process(q):
    """写进程"""
    print(f'我是写进程，我的pid是{os.getpid()}')
    for i in ['A', 'B', 'C']:
        print(f'把{i}放进队列')
        q.put(i)
        sleep(1)


def read_process(q):
    """读进程"""
    print(f'我是读进程，我的pid是:{os.getpid()}')
    while True:
        if not q.empty():
            value = q.get(True)
            print(f'我把{value}给取出来了')
            sleep(1)
        else:
            break


if __name__ == "__main__":
    q = Queue()  # 父进程实例化队列
    p_w = Process(target=write_process, args=(q,))
    p_r = Process(target=read_process, args=(q,))
    p_w.start()
    p_w.join()
    p_r.start()
    p_r.join()
