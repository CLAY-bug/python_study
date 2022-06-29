# 作者 ： 赖鑫
# 2022年06月20日19时17分43秒
import threading
from threading import Thread

g_num = 0


def work1(num):
    global g_num
    for i in range(num):
        mutex.acquire()  # 上锁
        g_num += 1
        mutex.release()  # 解锁
    print(f'----in work1----{g_num}')


def work2(num):
    global g_num
    for i in range(num):
        mutex.acquire()  # 上锁
        g_num += 1
        mutex.release()  # 解锁
    print(f'----in work2----{g_num}')


mutex = threading.Lock()
t1 = Thread(target=work1, args=(10000000,))
t2 = Thread(target=work2, args=(10000000,))
t1.start()
t2.start()
t1.join()
t2.join()
print(g_num)
