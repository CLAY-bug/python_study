# 作者: 王道 龙哥
# 2022年06月20日11时19分11秒
from collections.abc import Iterable, Iterator


class MyIterator(object):
    """
    自定义的供下面可迭代对象使用的一个迭代器
    当你对迭代器调用iter，返回类型必须是迭代器
    """

    def __init__(self, mylist):
        self.mylist = mylist
        # current用来记录当前访问到的位置
        self.current = 0

    def __next__(self):
        if self.current < len(self.mylist.container):
            item = self.mylist.container[self.current]
            self.current += 1
            return item
        else:
            raise StopIteration

    def __iter__(self):
        return self


class MyList(object):
    def __init__(self):
        self.container = []

    def add(self, item):
        self.container.append(item)

    def __iter__(self):
        """返回一个迭代器"""
        myiter = MyIterator(self)
        return myiter


mylist = MyList()
mylist.add(1)
mylist.add(2)
mylist.add(3)

print('-' * 50)
iter_mylist = iter(mylist)

for i in mylist:
    print(i)
