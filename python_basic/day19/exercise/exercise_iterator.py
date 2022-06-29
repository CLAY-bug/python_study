# 作者 ： 赖鑫
# 2022年06月20日20时19分53秒

class MyIterator:
    def __init__(self):
        self.container = []
        # 用来记录当前访问到的位置
        self.current = 0

    def add(self, item):
        self.container.append(item)

    def __next__(self):
        """
        当一个可迭代对象有了next方法，就是一个可迭代器
        :return: 
        """
        # 当现在位置小于容器总长度时，获取当前的值并返回
        if self.current < len(self.container):
            result = self.container[self.current]
            self.current += 1
            return result
        else:
            raise StopIteration

    def __iter__(self):  # 有个__iter__方法的对象，就是一个可迭代对象
        """
        返回一个迭代器,也就是返回自身
        """
        return self


my_iterator = MyIterator()
my_iterator.add(520)
my_iterator.add(890)
my_iterator.add(234)
my_iterator.add(567)
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
# for i in my_iterator:
#     print(i)
