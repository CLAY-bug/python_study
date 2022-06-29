# 作者 ： 赖鑫
# 2022年06月24日00时18分07秒

def select(arr, n):
    min_pos = 0
    i = 0
    while i < n - 1:
        j = i
        while j < n:
            if arr[min_pos] > arr[j]:
                min_pos = j
            j += 1
        arr[i], arr[min_pos] = arr[min_pos], arr[i]
        i += 1


if __name__ == '__main__':
    arr = [31, 42, 86, 59, 4, 61, 1, 34, 37, 12]
    select(arr, len(arr))
    print(arr)
