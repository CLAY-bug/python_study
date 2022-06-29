# 作者 ： 赖鑫
# 2022年06月20日19时44分02秒

from multiprocessing import Process
import time

num = [11, 22]


def work1():
    """子进程1"""
    for i in range(3):
        num.append(i)
        print(num)
        time.sleep(1)


def work2():
    """子进程2"""
    print(num)


if __name__ == '__main__':
    p1 = Process(target=work1)
    p1.start()
    p1.join()
    num.append(33)
    print(num)
    p2 = Process(target=work2)
    p2.start()
    p2.join()
