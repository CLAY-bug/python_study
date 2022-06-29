# 作者: 王道 龙哥
# 2022年06月20日10时16分00秒
import threading
import time


class MyThread(threading.Thread):
    def run(self):
        for i in range(3):
            time.sleep(1)
            msg = "I'm " + self.name + ' @ ' + str(i)
            print(msg)


def test():
    for i in range(5):
        t = MyThread()  # 创建了5个线程
        t.start()  # 启动线程


if __name__ == '__main__':
    test()
