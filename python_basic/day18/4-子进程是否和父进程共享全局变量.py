# 作者: 王道 龙哥
# 2022年06月18日10时20分01秒
from multiprocessing import Process
import os
import time

nums = [11, 22]


def work1():
    """子进程要执行的代码"""
    print("in process1 pid=%d ,nums=%s" % (os.getpid(), nums))
    for i in range(3):
        nums.append(i)
        time.sleep(1)
        print("in process1 pid=%d ,nums=%s" % (os.getpid(), nums))


def work2():
    """子进程要执行的代码"""
    print("in process2 pid=%d ,nums=%s" % (os.getpid(), nums))


if __name__ == '__main__':
    # 创建子进程，是自己的分身，子进程创建后全局变量的改变不会父亲
    p1 = Process(target=work1)
    p1.start()
    p1.join()
    print(nums)
    p2 = Process(target=work2)
    p2.start()
