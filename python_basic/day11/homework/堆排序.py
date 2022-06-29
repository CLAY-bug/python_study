# 作者 ： 赖鑫
# 2022年06月27日23时21分05秒

# 将待排序的序列构造成一个最大堆，此时序列的最大值为根节点
# 依次将根节点与待排序序列的最后一个元素交换
# 再维护从根节点到该元素的前一个节点为最大堆，如此往复，最终得到一个递增序列

def adjust_max_heap(arr, i, length):
    dad = i
    son = 2 * i + 1
    while son <= length:
        # 如果右孩子比左孩子大，就拿右孩子根父节点比
        if son + 1 <= length and arr[son] < arr[son + 1]:
            son += 1
        if arr[son] > arr[dad]:
            arr[son], arr[dad] = arr[dad], arr[son]
            dad = son
            son = 2 * dad + 1
        else:
            break


def heap_sort(arr):
    n = len(arr) - 1
    # 构建一个大根堆
    for i in range(n, -1, -1):
        adjust_max_heap(arr, i, n)
    # 把最顶端元素和最后一个元素交换,此时最后一个元素属于有序数
    arr[0], arr[n] = arr[n], arr[0]
    # 继续调整大根堆,从上往下调整，从0号元素开始
    for i in range(n - 1, 1, -1):
        adjust_max_heap(arr, 0, i)
        # 每次调整完就把最顶端元素和最后一个数进行交换
        arr[0], arr[i] = arr[i], arr[0]


if __name__ == '__main__':
    arr = [82, 5, 98, 95, 37, 39, 8, 37, 12, 35]
    heap_sort(arr)
    print(arr)
