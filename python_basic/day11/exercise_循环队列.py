# 作者 ： 赖鑫
# 2022年06月14日17时55分32秒

class Circle_queue:
    """循环队列"""

    def __init__(self, max_size):
        # 队列初始化大小
        self.max_size = max_size
        # 初始化元素的值
        self.arr = [0] * max_size
        # 指定front 和 rear 的位置
        self.front = 0
        self.rear = 0

    def enqueue(self, elem):
        """
        从尾部入队
        :param elem:
        :return:
        """
        # 入队之前判断是否队满
        if (self.rear + 1) % self.max_size == self.front:
            print("现在已经队满了，不能入队")
            return False
        self.arr[self.rear] = elem
        self.rear = (self.rear + 1) % self.max_size

    def dequeue(self):
        """
        从头部出队
        :return:
        """
        # 出队之前先判断队是否为空
        if self.rear == self.front:
            print("现在队列为空，不能出队")
        element = self.arr[self.front]
        # 将出队的元素所在位置的值置为-1,表示此位置没有值
        self.arr[self.front] = -1
        self.front = (self.front + 1) % self.max_size
        return element

    def size(self):
        return len(self.arr)


if __name__ == "__main__":
    # 实例化循环队列
    circle_queue = Circle_queue(6)
    circle_queue.enqueue(5)
    circle_queue.enqueue(2)
    circle_queue.enqueue(0)
    circle_queue.enqueue(2)
    circle_queue.enqueue(5)
    print(circle_queue.arr)
    print(f'删除的元素为：{circle_queue.dequeue()}')
    print(circle_queue.arr)
    print(circle_queue.size())
