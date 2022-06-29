# 作者 ： 赖鑫
# 2022年06月23日14时30分41秒

class Node:
    """节点类"""

    def __init__(self, elem=-1, lchild=None, rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild


class Tree:
    """树节点"""

    def __init__(self):
        """初始化根结点和辅助队列"""
        self.root = None
        self.arr = []

    def build(self, element):
        """使用层次建树的方法"""
        new_node = Node(element)  # 创建一个新结点
        self.arr.append(new_node)  # 将新结点入队
        if self.root is None:  # 判断根结点是否为空，是则把新结点作为根
            self.root = new_node
        else:
            if self.arr[0].lchild is None:  # 根结点不为空时，判断左孩子是否为空
                self.arr[0].lchild = new_node
            elif self.arr[0].rchild is None:  # 当左孩子不为空，右孩子为空时
                self.arr[0].rchild = new_node
                self.arr.pop(0)  # 当一个小树满了以后，把队首的元素给弹出

    def pre_order(self, node):
        """前序遍历"""
        if node:
            print(node.elem, end='')  # 先遍历根结点
            self.pre_order(node.lchild)  # 遍历左子树
            self.pre_order(node.rchild)  # 遍历右子树

    def min_order(self, node):
        """中序遍历"""
        if node:
            self.pre_order(node.lchild)  # 先遍历左子树
            print(node.elem, end='')  # 遍历根结点
            self.pre_order(node.rchild)  # 遍历右子树

    def last_order(self, node):
        if node:
            self.pre_order(node.lchild)  # 先遍历左子树
            self.pre_order(node.rchild)  # 遍历右子树
            print(node.elem, end='')  # 最后遍历根结点


if __name__ == '__main__':
    tree = Tree()  # 实例化一棵树
    for i in "abcdefghijk":
        tree.build(i)
    tree.pre_order(tree.root)
    print()
    tree.min_order(tree.root)
    print()
    tree.last_order(tree.root)
