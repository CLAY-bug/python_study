# 作者 ： 赖鑫
# 2022年06月14日17时42分56秒

from collections import deque


def use_dequeue():
    """
    使用双端队列
    :return:
    """
    queue = deque(['lx', 'lmx', 'xxx'])
    queue.append('ljj')
    queue.appendleft('dzq')
    print(queue)
    queue.popleft()
    queue.pop()
    print(queue)
    queue.reverse()
    print(queue)


if __name__ == "__main__":
    use_dequeue()

