# 作者: 王道 龙哥
# 2022年06月20日09时52分06秒
import threading
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
    # exit(1)  exit只是主线程终止了，还是会等子线程
    # sleep(5) # 屏蔽此行代码，试试看，程序是否会立马结束？
    t1.join()
    t2.join()
    print('---结束---:%s' % ctime())
