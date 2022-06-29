# 作者 ： 赖鑫
# 2022年06月18日13时14分22秒

from multiprocessing import Process
from time import sleep
import os

# 全局变量
nums = [11, 22]


def son1_processing():
    print(f'in process1 pid={os.getpid()}, nums={nums}')
    for i in range(3):
        nums.append(i)
        sleep(1)
        print(f'in process1 pid={os.getpid()}, nums={nums}')


def son2_processing():
    print(f'in process2 pid={os.getpid()}, nums={nums}')


if __name__ == '__main__':
    p1 = Process(target=son1_processing)
    p2 = Process(target=son2_processing)
    p1.start()
    # p1.join()  # 等待进程1执行完毕之后再继续
    p2.start()
