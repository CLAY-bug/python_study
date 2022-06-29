# 作者 ： 赖鑫
# 2022年06月21日17时23分50秒

import gevent


def f1(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        gevent.sleep(0.5)


def f2(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        gevent.sleep(0.5)


def f3(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        gevent.sleep(0.5)


g1 = gevent.spawn(f1, 5)
g2 = gevent.spawn(f2, 5)
g3 = gevent.spawn(f3, 5)
g1.join()
g2.join()
g3.join()
