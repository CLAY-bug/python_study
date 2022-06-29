# 作者: 王道 龙哥
# 2022年06月10日14时31分08秒

# 格式化代码的快捷键 ctrl+alt+L
import random


class MySort:
    def __init__(self, n, num_range):
        self.n = n  # 元素个数
        self.num_range = num_range
        self.arr = [random.randint(0, num_range) for i in range(n)]
        self.help_arr = [0] * n

    def bubble(self):
        i = self.n - 1
        arr = self.arr
        while i > 0:  # i在控制无序数的数目
            j = 0
            while j < i:  # 内层控制比较
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                j += 1
            i -= 1

    def select(self):
        i = 0
        arr = self.arr
        while i < self.n - 1:  # i不断的增大，无序数数目减少
            min_pos = i
            j = i + 1
            while j < self.n:  # 一轮比较下来，记录了最小值的下标
                if arr[j] < arr[min_pos]:
                    min_pos = j
                j += 1
            # 一轮比较以后，找到最小值和最前面进行交换
            arr[i], arr[min_pos] = arr[min_pos], arr[i]
            i += 1

    def insert(self):
        arr = self.arr
        i = 1
        while i < self.n:  # i依次拿的每一个无序数
            insert_val = arr[i]
            j = i - 1
            while j >= 0:  # 内层是一个有序序列，要把insert_val放入有序序列
                if insert_val < arr[j]:
                    arr[j + 1] = arr[j]
                else:
                    break
                j -= 1
            arr[j + 1] = insert_val
            i += 1

    def shell(self):
        arr = self.arr

        # 最外层循环控制步长
        gap = self.n >> 1
        while gap > 0:  # 将插入排序，5个为1的地方，改为gap
            i = gap
            while i < self.n:  # i依次拿的每一个无序数
                insert_val = arr[i]
                j = i - gap
                while j >= 0:  # 内层是一个有序序列，要把insert_val放入有序序列
                    if insert_val < arr[j]:
                        arr[j + gap] = arr[j]
                    else:
                        break
                    j -= gap
                arr[j + gap] = insert_val
                i += 1  # 这里不变
            gap = gap >> 1

    def partition(self, left, right):
        arr = self.arr
        k = left  # k始终指向要放置的比分割值小的元素的位置
        for i in range(left, right):
            if arr[i] < arr[right]:
                arr[k], arr[i] = arr[i], arr[k]
                k += 1
        arr[k], arr[right] = arr[right], arr[k]
        return k

    def quick(self, left, right):
        if left < right:
            pivot = self.partition(left, right)  # pivot是分割值的下标
            self.quick(left, pivot - 1)
            self.quick(pivot + 1, right)

    def adjust_max_heap(self, pos, len):
        """
        调整某个子树为大根堆
        :param pos:调整的子树的父亲
        :param len: 整个堆的元素个数
        :return:
        """
        arr = self.arr
        dad = pos
        son = 2 * dad + 1
        while son < len:
            # 让左孩子和右孩子比
            if son + 1 < len and arr[son] < arr[son + 1]:
                son += 1
            if arr[son] > arr[dad]:  # 拿孩子和父亲比，比父亲大，就交换
                arr[son], arr[dad] = arr[dad], arr[son]
                dad = son
                son = 2 * dad + 1
            else:
                break

    def heap(self):
        # 下面是把堆调整为大根堆的过程
        arr = self.arr
        for i in range(self.n // 2 - 1, -1, -1):  # 第一次调整为大根堆
            self.adjust_max_heap(i, self.n)
        arr[0], arr[self.n - 1] = arr[self.n - 1], arr[0]  # 交换顶部元素和最后一个元素
        for i in range(self.n - 1, 1, -1):
            self.adjust_max_heap(0, i)  # 把剩余元素调整为大根堆
            arr[0], arr[i - 1] = arr[i - 1], arr[0]

    def merge(self, low, mid, high):
        arr = self.arr
        help_arr = self.help_arr
        for i in range(low, high + 1):  # 先把数组里的内容拷贝到辅助数组里
            help_arr[i] = arr[i]
        i, j, k = low, mid + 1, low
        while i <= mid and j <= high:
            if help_arr[i] < help_arr[j]:
                arr[k] = help_arr[i]
                k += 1
                i += 1
            else:
                arr[k] = help_arr[j]
                k += 1
                j += 1
        while i <= mid:
            arr[k] = help_arr[i]
            k += 1
            i += 1
        while j <= high:
            arr[k] = help_arr[j]
            k += 1
            j += 1

    def merge_sort(self, low, high):
        if low < high:
            mid = (low + high) // 2
            self.merge_sort(low, mid)
            self.merge_sort(mid + 1, high)
            self.merge(low, mid, high)

    def test_sort(self, sort_method, *args, **kwargs):
        print(self.arr)
        sort_method(*args, **kwargs)
        print(self.arr)

    def use_range(self):
        for i in range(5, 0, -1):
            print(i)


if __name__ == '__main__':
    s = MySort(10, 99)
    # s.test_sort(s.quick, 0, s.n - 1)  # 方法传递不要加括号
    # s.test_sort(s.heap)
    # s.test_sort(s.merge_sort, 0, s.n-1)
    s.test_sort(s.bubble)
