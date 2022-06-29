# 作者 ： 赖鑫
# 2022年06月23日09时18分29秒

class CircleQueue:
    def __init__(self, max_size):
        """
        初始化循环队列
        :param max_size: 传入队列最大值
        """
        self.arr = [0] * max_size
        self.max_size = max_size
        self.front = 0  # 初始队头队尾都在0的位置
        self.rear = 0

    def enqueue(self, element):
        """
        元素入队
        :param element:传入要添加到队列的元素
        :return:
        """
        # 入队前判断队列是否满
        if (self.rear + 1) % self.max_size == self.front:
            print("队列已满，不能继续添加元素了")
            return False
        self.arr[self.rear] = element
        self.rear = (self.rear + 1) % self.max_size

    def dequeue(self):
        """
        元素出队
        :return: 返回出队的元素
        """
        # 出队之前先判断是否为空
        if self.rear == self.front:
            print("队列为空，不能出队")
            return False
        element = self.arr[self.front]
        self.arr[self.front] = None  # 将出队的位置值为空，表示此位置没有元素
        self.front = (self.front + 1) % self.max_size
        return element

    def size(self):
        """
        :return:显示剩余空间
        """
        size = (self.rear - self.front + self.max_size) % self.max_size
        print(f"当前队列中有{size}个元素")


circle = CircleQueue(5)
circle.size()
circle.enqueue(15)
circle.enqueue(89)
circle.enqueue(67)
print(f'{circle.dequeue()}出队了')
circle.enqueue(100)
circle.enqueue(324)
circle.enqueue(56)  # 队满来
print(circle.arr)
circle.size()  # 当前有4个元素
