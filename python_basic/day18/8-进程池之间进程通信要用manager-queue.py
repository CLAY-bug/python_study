# 作者: 王道 龙哥
# 2022年06月18日11时31分07秒
# 修改import中的Queue为Manager
from multiprocessing import Manager, Pool
import os, time, random


def reader(q):
    print("reader启动(%s),父进程为(%s)" % (os.getpid(), os.getppid()))
    for i in range(q.qsize()):
        print("reader从Queue获取到消息：%s" % q.get(True))


def writer(q):
    print("writer启动(%s),父进程为(%s)" % (os.getpid(), os.getppid()))
    for i in "wangdao":
        q.put(i)
    time.sleep(3)


if __name__ == "__main__":
    print("(%s) start" % os.getpid())
    q = Manager().Queue()  # 使用Manager中的Queue
    po = Pool()  # 如果进程池中不设置进程数，每次派一个任务，就会启动一个进程
    po.apply_async(writer, (q,))

    time.sleep(1)  # 先让上面的任务向Queue存入数据，然后再让下面的任务开始从中取数据

    po.apply_async(reader, (q,))
    po.close()
    po.join()
    print("(%s) End" % os.getpid())
