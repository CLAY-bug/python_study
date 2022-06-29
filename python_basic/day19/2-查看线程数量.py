# 作者: 王道 龙哥
# 2022年06月20日10时00分11秒
import threading
import time
from time import sleep, ctime


def sing():
    for i in range(5):
        print("正在唱歌...%d" % i)
        sleep(1)


def dance():
    for i in range(5):
        print("正在跳舞...%d" % i)
        sleep(1)


if __name__ == '__main__':
    print('---开始---:%s' % ctime())

    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)

    t1.start()
    t2.start()

    while True:
        num = len(threading.enumerate())
        print(num)
        if num <= 1:
            break
        time.sleep(0.5)
    print('---结束---:%s' % ctime())
