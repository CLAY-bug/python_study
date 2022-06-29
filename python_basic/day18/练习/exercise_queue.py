# 作者 ： 赖鑫
# 2022年06月19日22时04分53秒

from multiprocessing import Queue, Process
from time import sleep


def write(q):
    for i in range(10):
        if not q.full():
            q.put(i)


def read(q):
    while True:
        if not q.empty():
            print(f'i get {q.get()}')
            sleep(1)
        else:
            break


if __name__ == '__main__':
    q = Queue()
    p_w = Process(target=write, args=(q,))
    p_r = Process(target=read, args=(q,))
    p_w.start()
    p_w.join()
    p_r.start()
    p_r.join()
