# 作者 ： 赖鑫
# 2022年06月18日21时23分48秒

from threading import Thread


def while1():
    """子线程"""
    while True:
        pass


if __name__ == '__main__':
    t = Thread(target=while1)
    t.start()
    # 主线程
    while True:
        pass
