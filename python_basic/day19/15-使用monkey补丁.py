# 作者: 王道 龙哥
# 2022年06月20日15时30分25秒
from gevent import monkey
import gevent
import random
import time
monkey.patch_all()  #放在代码最前面
def coroutine_work(coroutine_name):
    for i in range(10):
        print(coroutine_name, i)
        time.sleep(random.random())  #模拟I/O阻塞时间不确定

gevent.joinall([
        gevent.spawn(coroutine_work, "work1"),
        gevent.spawn(coroutine_work, "work2")
])
