# 作者: 王道 龙哥
# 2022年06月18日11时03分28秒
from multiprocessing import Process,Queue
import time

def writer(q:Queue):
    for i in ['A','B','C']:
        print('writer write')
        q.put(i)
        time.sleep(1)

def reader(q:Queue):
    while True:
        if not q.empty():
            value = q.get(True)
            print('Get %s from queue.' % value)
            time.sleep(2)
        else:
            break

if __name__ == '__main__':
    q=Queue() #不放置默认是最大的
    pw=Process(target=writer,args=(q,))
    pw.start()
    time.sleep(0.5)
    pr=Process(target=reader,args=(q,))
    pr.start()
    pw.join()
    pr.join()