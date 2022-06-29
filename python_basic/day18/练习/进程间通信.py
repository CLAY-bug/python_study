# 作者 ： 赖鑫
# 2022年06月18日13时52分14秒

from multiprocessing import Process
from multiprocessing import Queue

q = Queue(10)
q.put("消息1")
q.put("消息2")
# 写消息时，先判断队列是否已满，再进行写入
while True:
    if not q.full():
        q.put_nowait()
    else:
        print("消息队列已满")
        break
# 读消息时，先判断队列已空，在读取
while True:
    if not q.empty():
        for i in range(q.qsize()):
            print(q.get_nowait())
