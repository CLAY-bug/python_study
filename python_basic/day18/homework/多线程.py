# 作者 ： 赖鑫
# 2022年06月18日20时49分16秒
import time
from threading import Thread


def say_hello():
    print('我想给你说hello')
    time.sleep(1)


if __name__ == '__main__':
    for i in range(10):
        t = Thread(target=say_hello)  # 创建线程
        t.start()
