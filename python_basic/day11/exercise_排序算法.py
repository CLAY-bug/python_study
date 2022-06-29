# 作者 ： 赖鑫
# 2022年06月15日21时25分57秒

import random


class Mysort:
    def __init__(self, n, num_range):
        self.n = n  # 一起共会生成n个数
        self.num_range = num_range  # 生成数的范围
        self.arr = [random.randint(0, num_range) for _ in range(n)]

    def bubble(self):
        """冒泡排序"""
        i = self.n - 1  # 外层控制无序数的数目，内层进行比较
        arr = self.arr
        while i > 0:  # 当i=1时，j=0，比较arr[0]和arr[1]
            j = 0
            while j < i:
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                j += 1
            i -= 1

    def select(self):
        """选择排序"""
        i = 0
        n = self.n
        arr = self.arr
        while i < n - 1:  # i之前都是有序数
            min_pos = i
            j = i + 1
            while j < n:  # 一轮下来记录了最小值的下标
                if arr[j] < arr[min_pos]:
                    min_pos = j
                j += 1
            arr[i], arr[min_pos] = arr[min_pos], arr[i]  # 一轮比较以后，让第i个数与最小值交换
            i += 1  # i不断的增大，无序数不断的减少
            print(arr)

    def insert(self):
        """插入排序"""
        arr = self.arr
        n = self.n
        i = 1  # 默认arr[0]为有序元素，所有从arr[1]开始往前插
        while i < n:
            j = i - 1  # i之前的元素都是有序的，每次把第i个元素往前插
            insert_val = arr[i]  # 把要插入的元素先保存起来
            while j >= 0:
                if arr[j] > insert_val:  # 如果当前元素大于要插入元素，把元素往后移动一位
                    arr[j + 1] = arr[j]
                    j -= 1
                else:
                    break  # 如果当前元素已经比要插入的元素小了，说明前面的所有元素都比要插入的元素小了
            arr[j + 1] = insert_val  # 一轮循环结束，把要插入值插入当前空余位置
            i += 1  # 继续把后续元素往前插

    def shell(self):
        """希尔排序"""
        arr = self.arr
        gap = self.n >> 1  # 右移运算相当于除二，但是更快
        while gap > 0:  # 把插入排序的五个一改为gap即为希尔排序
            i = gap
            while i < self.n:
                j = i - gap
                insert_val = arr[i]
                while j >= 0:
                    if arr[j] > insert_val:
                        arr[j + gap] = arr[j]
                        j -= gap
                    else:
                        break
                arr[j + gap] = insert_val
                i += 1
            gap >>= 1

    def partition(self, left, right) -> int:
        """快排分割函数"""
        arr = self.arr
        i = left  # 用来进行遍历
        k = left  # 用来记录pivot的位置，k的左边都比pivot小，k的右边都比pivot大
        while i < right:
            if arr[i] < arr[right]:
                arr[i], arr[k] = arr[k], arr[i]
                k += 1
            i += 1
        arr[k], arr[right] = arr[right], arr[k]
        return k

    def quick_sort(self, left, right):
        """快速排序"""
        if left < right:
            pivot = self.partition(left, right)
            self.quick_sort(left, pivot - 1)
            self.quick_sort(pivot + 1, right)

    def sort_test(self, sort_method, *args, **kwargs):
        print(f"排序之前：")
        print(self.arr)
        sort_method(*args, **kwargs)
        print(f"排序之后：")
        print(self.arr)


if __name__ == "__main__":
    my_sort = Mysort(10, 99)  # 生成20个数，范围在0-99之间
    # my_sort.sort_test(my_sort.bubble)  # 冒泡排序
    # my_sort.sort_test(my_sort.select)  # 选择排序
    # my_sort.sort_test(my_sort.insert)  # 插入排序
    # my_sort.sort_test(my_sort.shell)  # 希尔排序
    my_sort.sort_test(my_sort.quick_sort, 0, my_sort.n - 1)  # 快速排序
