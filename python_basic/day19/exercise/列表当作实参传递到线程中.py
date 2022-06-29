# 作者 ： 赖鑫
# 2022年06月20日19时05分44秒
import time
from threading import Thread
from time import sleep

g_nums = [11, 22, 33]


def work1(nums: list):
    nums.append(44)
    print(f'----in work1----{nums}')


def work2(nums: list):
    sleep(1)
    print(f'----in work2----{nums}')


t1 = Thread(target=work1, args=(g_nums,))
t1.start()

t2 = Thread(target=work2, args=(g_nums,))
t2.start()
