# 作者 ： 赖鑫
# 2022年06月20日20时04分43秒
import threading
from threading import Thread
from time import sleep

g_num = 0


def work_A(num):
    global g_num
    for i in range(num):
        mutexA.acquire()  # 对A上锁，进行加法
        g_num += 1
        sleep(1)
        mutexB.acquire()  # 对B上锁
        print('我要对B上锁')
        mutexB.release()
        mutexA.release()  # 解锁
    print(f'----in work1----{g_num}')


def work_B(num):
    global g_num
    for i in range(num):
        mutexB.acquire()  # 对B上锁
        g_num += 1
        sleep(1)
        mutexA.acquire()  # 对A上锁
        print('我要对A上锁')
        mutexA.release()
        mutexB.release()  # 解锁
    print(f'----in work2----{g_num}')


mutexA = threading.Lock()
mutexB = threading.Lock()
t1 = Thread(target=work_A, args=(10000000,))
t2 = Thread(target=work_B, args=(10000000,))
t1.start()
t2.start()
t1.join()
t2.join()
print(g_num)
