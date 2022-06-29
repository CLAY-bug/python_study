# 作者 ： 赖鑫
# 2022年06月18日12时52分37秒

from multiprocessing import Process
import time
import os


def son_process():
    """子进程"""
    print(f'子进程运行中，子进程的pid为：{os.getpid()}')
    print(f'我父亲的pid为: {os.getppid()}')
    print('子进程将要结束了')


if __name__ == '__main__':
    print(f'父进程pid：{os.getpid()}')
    p = Process(target=son_process)
    p.start()
    p.terminate()
    time.sleep(20)
    p.join()
    time.sleep(20)
