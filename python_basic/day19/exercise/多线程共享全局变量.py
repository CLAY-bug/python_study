# 作者 ： 赖鑫
# 2022年06月20日18时56分35秒
from threading import Thread
import time

g_num = 100


def work1():
    global g_num
    for i in range(3):
        g_num += 1

    print(f'---in work1 ,g_num is {g_num}')


def work2():
    global g_num
    print(f'---in work2, g_num is {g_num}')


print(f'---创建线程之前,g_num is {g_num}')
t1 = Thread(target=work1)
t1.start()

time.sleep(1)

t2 = Thread(target=work2)  # 说明线程之间是可以共享全局变量的
t2.start()
