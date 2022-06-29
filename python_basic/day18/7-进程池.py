# 作者: 王道 龙哥
# 2022年06月18日11时18分38秒
from multiprocessing.pool import Pool

import os, time, random


# 具体干的任务就是模拟睡觉一段时间
def worker(msg):
    t_start = time.time()
    print("%s开始执行,进程号为%d" % (msg, os.getpid()))
    # random.random()随机生成0~1之间的浮点数
    time.sleep(random.random() * 2)
    t_stop = time.time()
    print(msg, "执行完毕，耗时%0.2f" % (t_stop - t_start))


if __name__ == '__main__':
    po = Pool(3)
    for i in range(10):
        po.apply_async(worker, (i,))  # worker是干什么活，i哪一个客户
    print("----start----")
    po.close()
    # po.terminate()  # 关闭进程池，关闭后po不再apply_async新的请求
    print('close 之后')
    po.join()  # 等待po中所有子进程完成队列里的所有任务，必须放在close语句之后
    print("-----end-----")
    