# 作者: 王道 龙哥
# 2022年06月18日11时47分41秒
import time
from threading import Thread


def say_sorry():
    print("亲爱的，我错了，我能吃饭了吗？")
    time.sleep(1)


if __name__ == "__main__":
    for i in range(5):
        t = Thread(target=say_sorry)
        t.start()
