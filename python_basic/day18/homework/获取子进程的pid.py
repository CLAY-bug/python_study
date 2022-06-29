# 作者 ： 赖鑫
# 2022年06月18日16时06分22秒
from multiprocessing import Process
import os


def son_process():
    """子进程"""
    print(f"我是子进程，这是我的pid：{os.getpid()}")
    print(f"这是我父亲的pid:{os.getppid()}")


if __name__ == '__main__':
    print(f"我是父进程，这是我的pid:{os.getpid()}")
    p = Process(target=son_process)
    p.start()
