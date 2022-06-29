# 作者 ： 赖鑫
# 2022年06月15日09时08分50秒

# 定义节点类
class Node:
    """节点类"""
    def __init__(self, elem=-1, lchild=None, rchild=None):  # 初始化节点
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild


class Tree:
    """树类"""
    def __init__(self):  # 初始化树，设根结点和辅助队列
        self.root = None
        self.queue = []

    def build(self, element):
        """
        建树
        :return:
        """
        new_node = Node(element)  # 创建一个新节点,并将它入队
        self.queue.append(new_node)
        if self.root is None:
            self.root = new_node
            self.queue[0] = new_node
        else:
            if self.queue[0].lchild is None:
                self.queue[0].lchild = new_node
            elif self.queue[0].rchild is None:
                self.queue[0].rchild = new_node
                self.queue.pop(0)  # 当一颗二叉树满了之后把第一个节点弹出

    def pre_order(self, node):
        """
        前序遍历
        :return:
        """
        if node:  # 如果传入的节点不为空，则可以遍历
            print(node.elem, end='')
            self.pre_order(node.lchild)
            self.pre_order(node.rchild)

    def mid_order(self, node):
        """
        中序遍历
        :param node:
        :return:
        """
        if node:
            self.mid_order(node.lchild)
            print(node.elem, end='')
            self.mid_order(node.rchild)


    def last_order(self, node):
        """
        后序遍历
        :param node:
        :return:
        """
        if node:
            self.mid_order(node.lchild)
            self.mid_order(node.rchild)
            print(node.elem, end='')


if __name__ == "__main__":
    tree = Tree()
    for i in "abcdefg":
        tree.build(i)
    print("前序遍历:")
    tree.pre_order(tree.root)
    print("\n中序遍历:")
    tree.mid_order(tree.root)
    print("\n后序遍历:")
    tree.last_order(tree.root)
