# 作者 ： 赖鑫
# 2022年06月24日00时29分29秒

def insert(arr, n):
    i = 1
    while i < n:
        j = i - 1
        insert_val = arr[i]
        while j >= 0:
            if insert_val > arr[j]:
                break
            else:
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = insert_val
        i += 1


if __name__ == '__main__':
    arr = [77, 50, 50, 91, 15, 86, 72, 59, 3, 22]
    insert(arr, len(arr))
    print(arr)
