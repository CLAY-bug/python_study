# 作者 ： 赖鑫
# 2022年06月14日21时24分05秒

# 用链表的方式建树
class Node:
    """二叉树所需要的节点类"""
    def __init__(self, elem=-1, lchild=None, rchild=None):
        self.elem = elem
        self.lchild = lchild  # 左孩子
        self.rchild = rchild  # 右孩子


class Tree:
    """树类"""
    def __init__(self):
        # 初始化树，包括根结点和辅助队列
        self.root = None
        # 辅助队列实际上用来存储树的节点
        self.queue = []

    def build_tree(self, element):
        # 先创建一个新节点
        new_node = Node(element)
        # 将新节点放入队列
        self.queue.append(new_node)
        # 将新节点放入树中
        if self.root is None:  # 判断树是否为空
            self.root = new_node  # 为空则传入新节点
        else:  # 如果树不为空，判断队列第一个元素的左孩子是否为空
            if self.queue[0].lchild is None:  # 左孩子为空，则把新节点赋给左孩子
                self.queue[0].lchild = new_node
            elif self.queue[0].rchild is None:  # 如果左边不为空，右孩子为空，则把新节点赋给右孩子
                self.queue[0].rchild = new_node
                self.queue.pop(0)  # 如果右边也放了元素，把队列第一个元素弹出

    def pre_order(self, node):
        """遍历顺序，根左右"""
        if node:
            print(node.elem, end='')
            self.pre_order(node.lchild)
            self.pre_order(node.rchild)




if __name__ == "__main__":
    # 实例化一棵树
    tree = Tree()
    for i in "abcdefg":
        tree.build_tree(i)
    tree.pre_order(tree.root)

