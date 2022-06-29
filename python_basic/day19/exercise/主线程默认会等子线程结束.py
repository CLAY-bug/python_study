# 作者 ： 赖鑫
# 2022年06月20日17时11分36秒
import os
import threading
import time
from time import sleep, ctime


class MyThread(threading.Thread):
    def run(self) -> None:
        for i in range(3):
            time.sleep(1)
            msg = 'i am ' + self.name + str(i)
            print(msg)


if __name__ == '__main__':
    t = MyThread()
    t.start()  # start中调用了run方法
