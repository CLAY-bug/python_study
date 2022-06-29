# 作者 ： 赖鑫
# 2022年06月27日22时22分15秒

# 快排
def partition(arr, left, right) -> int:
    i = left  # 用来遍历
    k = left  # 用来记录比pivot小的位置
    while i < right:
        if arr[i] < arr[right]:
            arr[i], arr[k] = arr[k], arr[i]
            k += 1
        i += 1
    arr[k], arr[right] = arr[right], arr[k]
    return k


def quick_sort(arr, left, right):
    if left < right:
        pivot = partition(arr, left, right)
        quick_sort(arr, left, pivot - 1)
        quick_sort(arr, pivot + 1, right)


if __name__ == '__main__':
    arr = [46, 51, 89, 33, 56, 94, 22, 56, 4, 27]
    quick_sort(arr, 0, len(arr) - 1)
    print(arr)
