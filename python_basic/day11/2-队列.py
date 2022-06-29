# 作者: 王道 龙哥
# 2022年06月10日10时09分12秒
from collections import deque


def use_deque():
    """
    使用双端队列
    :return:
    """
    # 增删查改
    queue = deque(["Eric", "John", "Michael"])
    queue.append('luke')
    print(queue)
    print(queue.popleft())  # 右边删除就是pop
    print(queue)

    queue[0] = 'xiongda'
    print(queue)


class CircleQueue:
    def __init__(self, max_size):
        self.max_size = max_size
        self.arr = [0] * max_size
        self.front = 0
        self.rear = 0

    def enqueue(self, element):
        """
        入队，往尾部放
        :return:
        """
        # 判断队列是否满了，满了就不放
        if (self.rear + 1) % self.max_size == self.front:
            print('队列满了')
            return False
        self.arr[self.rear] = element
        self.rear = (self.rear + 1) % self.max_size
        return True

    def dequeue(self):
        if self.rear == self.front:
            print('队列为空')
            return False
        element = self.arr[self.front]
        self.front = (self.front + 1) % self.max_size
        return element


if __name__ == '__main__':
    # use_deque()
    c = CircleQueue(5)
    c.enqueue(1)
    c.enqueue(2)
    c.enqueue(3)
    c.enqueue(4)
    print(c.dequeue())
    print(c.arr)
