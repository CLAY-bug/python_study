# 作者: 王道 龙哥
# 2022年06月10日10时53分15秒
class Node(object):
    """节点类"""

    def __init__(self, elem=-1, lchild=None, rchild=None):
        self.elem = elem
        self.lchild = lchild  # 左孩子
        self.rchild = rchild  # 右孩子


class Tree:
    def __init__(self):
        self.root = None
        self.queue = []

    def build_tree(self, element):
        new_node = Node(element)
        # 新元素放入队列
        self.queue.append(new_node)
        # 新结点放入树中
        if self.root is None:
            self.root = new_node  # 树为空，新结点就是树根
        else:
            if self.queue[0].lchild is None:  # 先判断左边为不为空
                self.queue[0].lchild = new_node
            elif self.queue[0].rchild is None:
                self.queue[0].rchild = new_node
                self.queue.pop(0)  # 放到右边，元素满了，就弹出去

    def preorder(self, node):
        """
        前序遍历
        :param node:
        :return:
        """
        if node:
            print(node.elem, end='')
            self.preorder(node.lchild)
            self.preorder(node.rchild)

    def midorder(self, node):
        if node:
            self.midorder(node.lchild)
            print(node.elem, end='')
            self.midorder(node.rchild)

    def lastorder(self, node):
        if node:
            self.lastorder(node.lchild)
            self.lastorder(node.rchild)
            print(node.elem, end='')


if __name__ == '__main__':
    tree = Tree()
    for i in 'abcdefghij':
        tree.build_tree(i)
    tree.preorder(tree.root)
    print()
    # tree.midorder(tree.root)
    # print()
    # tree.lastorder(tree.root)
    # print()
