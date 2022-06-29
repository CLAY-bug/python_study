# 作者: 王道 龙哥
# 2022年06月13日16时02分17秒
RED = 0
BLACK = 1
class RedBlackTreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.p = None  #结点必须有指向父亲的
        self.color = RED

#传递tree是因为node本身可能是树根
def left_rotate(tree, node:RedBlackTreeNode):
    if not node.right:
        return False
    node_right = node.right
    node_right.p = node.p
    if not node.p:#如果node没有父亲，node_right就是新的根
        tree.root = node_right
    elif node == node.p.left:
        node.p.left = node_right
    else:
        node.p.right = node_right
    if node_right.left:
        node_right.left.p = node
    node.right = node_right.left
    node.p = node_right
    node_right.left = node

#y就是node，x就是node_left
def right_rotate(tree, node):
    if not node.left:
        return False
    node_left = node.left
    node_left.p = node.p
    if not node.p:
        tree.root = node_left
    elif node == node.p.left:
        node.p.left = node_left
    elif node == node.p.right:
        node.p.right = node_left
    if node_left.right:
        node_left.right.p = node
    node.left = node_left.right
    node.p = node_left
    node_left.right = node

#key就是父亲的值，direction是左边还是右边
def rbtree_print(node, key, direction):
    if node:
        if direction == 0:  # tree是根节点
            print("%2d(B) is root" % node.value)
        else:  # tree是分支节点
            print("%2d(%s) is %2d's %6s child" % (
                node.value, ("B" if node.color == 1 else "R"), key, ("right" if direction == 1 else "left")))

        rbtree_print(node.left, node.value, -1)
        rbtree_print(node.right, node.value, 1)


class RedBlackTree:
    def __init__(self):
        self.root:RedBlackTreeNode=None

    def __insert_fixup(self,node):
        parent:RedBlackTreeNode=node.p
        while parent and parent.color==0:

            gparent:RedBlackTreeNode=parent.p
            if parent is gparent.left:
                uncle:RedBlackTreeNode=gparent.right
                # 情形三
                if uncle and uncle.color==RED:
                    parent.color=BLACK
                    uncle.color=BLACK
                    gparent.color=RED
                    node=gparent
                    parent=node.p
                    continue
                if node is parent.right: #情形四
                    left_rotate(self,parent)
                    parent,node=node,parent
                right_rotate(self,gparent)  #情形五
                parent.color=BLACK
                gparent.color=RED
            else:
                uncle: RedBlackTreeNode = gparent.left
                # 情形三
                if uncle and uncle.color == RED:
                    parent.color = BLACK
                    uncle.color = BLACK
                    gparent.color = RED
                    node = gparent
                    parent = node.p
                    continue
                if node is parent.left:  # 情形四
                    right_rotate(self, parent)
                    parent, node = node, parent
                left_rotate(self, gparent)  # 情形五
                parent.color = BLACK
                gparent.color = RED

        self.root.color=BLACK

    def insert(self,node:RedBlackTreeNode):
        #第一步 放入结点，第二步 调整
        if self.root is None:
            self.root=node
        else:
            current_node=self.root
            while current_node:
                parent=current_node
                if current_node.value>node.value:
                    current_node=current_node.left
                else:
                    current_node=current_node.right
            #接下来知道了node的父亲是parent
            node.p=parent
            if parent.value >node.value:
                parent.left=node
            else:
                parent.right=node

        self.__insert_fixup(node)


def main():
    number_list = (7, 4, 1, 8, 5, 2, 9, 6, 3)
    tree = RedBlackTree()
    for number in number_list:
        node = RedBlackTreeNode(number)
        tree.insert(node)
        # rbtree_print(tree.root, 0, 0)  #如果树不对，就每一个结点放进去就打一下
    rbtree_print(tree.root, 0, 0)
if __name__ == '__main__':
    main()