# 作者 ： 赖鑫
# 2022年06月17日22时15分47秒

from multiprocessing import Process
import time


def son_process():
    """子进程"""
    while True:
        print("我是子进程-----")
        time.sleep(1)


if __name__ == '__main__':
    p = Process(target=son_process)
    p.start()
    while True:
        print("我是父进程-----")
        time.sleep(1)
