# 作者 ： 赖鑫
# 2022年06月21日17时14分20秒
from greenlet import greenlet
from time import sleep


def work1():
    while True:
        print('----work1----')
        gr2.switch()  # 切换成work2
        sleep(0.5)


def work2():
    while True:
        print('----work2----')
        gr1.switch()  # 切换成work1
        sleep(0.5)


gr1 = greenlet(work1)
gr2 = greenlet(work2)
gr1.switch()  # 先调用work1
