# 作者: 王道 龙哥
# 2022年06月20日10时20分58秒
from threading import Thread, Lock
import time

num = 0


def work1(mutex):
    global num
    for i in range(1000000):
        mutex.acquire()
        num += 1
        mutex.release()


def work2(mutex):
    global num
    for i in range(1000000):
        mutex.acquire()
        num += 1
        mutex.release()


def main():
    # 创建锁
    mutex = Lock()
    t1 = Thread(target=work1, args=(mutex,))
    t1.start()
    t2 = Thread(target=work2, args=(mutex,))
    t2.start()
    t1.join()
    t2.join()
    print(num)


if __name__ == '__main__':
    main()
