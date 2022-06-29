# 作者: 王道 龙哥
# 2022年06月20日10时20分58秒
from threading import Thread
import time

num = 0


def work1():
    global num
    for i in range(1000000):
        num += 1


def work2():
    global num
    for i in range(1000000):
        num += 1


if __name__ == '__main__':
    t1 = Thread(target=work1)
    t1.start()
    t2 = Thread(target=work2)
    t2.start()
    t1.join()
    t2.join()
    print(num)
