# 作者 ： 赖鑫
# 2022年06月24日00时03分22秒
def bubble(arr, n):
    i = n - 1
    while i >= 0:
        j = 0
        while j < i:
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            j += 1
        i -= 1


if __name__ == '__main__':
    arr = [58, 49, 83, 62, 97, 69, 34, 0, 41, 55]
    bubble(arr, len(arr))
    print(arr)
