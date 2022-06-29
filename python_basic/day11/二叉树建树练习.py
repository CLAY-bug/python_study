# 作者 ： 赖鑫
# 2022年06月15日20时02分09秒

class Node:
    """节点类"""
    def __init__(self, elem=-1, lchild=None, rchild=None):
        """初始化节点"""
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild


class Tree:
    """树类"""
    def __init__(self):
        """初始化根结点和辅助队列"""
        self.root = None
        self.queue = []

    def build(self, element):
        """建树"""
        new_node = Node(element)  # 先创建一个新节点
        self.queue.append(new_node)  # 将新节点入队
        # 判断树是否为空
        if self.root is None:
            self.root = new_node  # 如果树为空，让新节点作为树根
        else:
            if self.queue[0].lchild is None:
                self.queue[0].lchild = new_node
            elif self.queue[0].rchild is None:
                self.queue[0].rchild = new_node
                self.queue.pop(0)  # 如果左右孩子都有了，则把这个元素出队

    def pre_order(self, node):
        if node:
            print(node.elem, end='')
            self.pre_order(node.lchild)
            self.pre_order(node.rchild)

    def mid_order(self, node):
        if node:
            self.pre_order(node.lchild)
            print(node.elem, end='')
            self.pre_order(node.rchild)

    def last_order(self, node):
        if node:
            self.pre_order(node.lchild)
            self.pre_order(node.rchild)
            print(node.elem, end='')


if __name__ == "__main__":
    tree = Tree()
    # 建树
    for i in 'abcdefg':
        tree.build(i)
    tree.pre_order(tree.root)
