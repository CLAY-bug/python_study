# 作者 ： 赖鑫
# 2022年06月14日17时10分47秒

class Queue:
    def __init__(self):
        self.queue = []

    # 入队
    def enqueue(self, elem):
        self.queue.append(elem)

    # 出队,只能从队列头出队，即弹出第一个元素
    def dequeue(self):
        self.queue.pop(0)


# 实例化一个队列
queue = Queue()
queue.enqueue(5)
queue.enqueue(2)
queue.enqueue(0)
print(queue.queue)
queue.dequeue()
print(queue.queue)
