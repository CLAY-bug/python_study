# 作者 ： 赖鑫
# 2022年06月14日16时08分23秒

class Stack:
    """实现一个栈"""
    # 初始化栈，为空列表
    def __init__(self):
        self.stack = []

    # 压栈操作,使元素进栈
    def push(self, elem):
        self.stack.append(elem)

    # 弹栈,使元素出栈
    def pop(self):
        self.stack.pop()

    # 获取栈顶元素
    def get_top(self):
        if not self.stack:
            return "栈为空!"
        else:
            return self.stack[-1]

    # 获取栈的大小
    def get_size(self):
        return len(self.stack)


if __name__ == "__main__":
    # 实例化一个栈
    stack = Stack()
    stack.push(5)
    stack.push(2)
    stack.push(0)
    top = stack.get_top()
    print(top)
    stack.pop()
    stack.push(0)
    print(stack.stack)
