# 作者 ： 赖鑫
# 2022年06月18日19时42分39秒

import os
import time
from multiprocessing import Manager, Pool


def writer(q):
    """写进程"""
    print(f"我是写进程：{os.getpid()},父进程为:{os.getppid()}")
    for i in ['A', 'B', 'C', 'D']:
        q.put(i)
    time.sleep(2)


def reader(q):
    """读进程"""
    print(f'我是写进程:{os.getpid()}, 父进程为:{os.getppid()}')
    while True:
        if not q.empty():
            print(f"我读取了{q.get()}")
        else:
            break


if __name__ == '__main__':
    pool = Pool()  # 定义进程池
    q = Manager().Queue()  # 实例化进程池中的队列
    print("start--------")
    pool.apply_async(writer, (q,))  # 给写进程分配任务
    time.sleep(1)
    pool.apply_async(reader, (q,))  # 给读进程非配任务
    pool.close()
    pool.join()  # 等待所有任务完成，再继续
    print("end----------")
