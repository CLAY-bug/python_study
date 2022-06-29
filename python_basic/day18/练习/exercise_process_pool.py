# 作者 ： 赖鑫
# 2022年06月19日22时40分42秒

from multiprocessing import Pool
import time, os, random


def worker(msg):
    t_start = time.time()
    print(f'{msg}开始工作，进程号为：{os.getpid()}')
    # random.random()随机生成0~1之间的浮点数
    time.sleep(random.random() * 2)
    t_stop = time.time()
    print(f'{msg}工作完毕,用时{t_stop - t_start}')


if __name__ == '__main__':
    pool = Pool(10)
    for i in range(11):
        pool.apply_async(worker, (i,))
    print("----start----")
    pool.close()
    pool.join()
    print("-----end-----")
