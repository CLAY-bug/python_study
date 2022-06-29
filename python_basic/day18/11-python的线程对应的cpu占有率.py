# 作者: 王道 龙哥
# 2022年06月18日11时49分24秒
from threading import Thread


def while1():
    while True:
        pass


if __name__ == '__main__':
    t = Thread(target=while1)
    t.start()
    while True:
        pass
