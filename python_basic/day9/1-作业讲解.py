# 作者: 王道 龙哥
# 2022年06月08日10时01分29秒

# 8个数找出现1次的那2个数，剩余的6个是3对数
def find_two():
    list1 = [3, 4, 5, 11, 6, 3, 4, 5]
    # 把所有的数异或，得到的是11和6的异或值
    result = 0
    for i in list1:
        result ^= i
    # 找出result最低位不为0的那个值
    splice_flag = result & -result
    result1 = 0
    result2 = 0
    for i in list1:
        if i & splice_flag:  # splice_flag可以把11和6分到不同的两堆
            result1 ^= i
        else:
            result2 ^= i
    print(result1, result2)


# day5 给定一个n个整型元素的列表a，其中有一个元素出现次数超过n / 2，求这个元素
# 选举
# 火拼
def find_half():
    list1 = [1, 6, 6, 6, 2, 3, 6, 6, 4]
    vote_num = 0
    x = list1[0]  # x要投票给谁,x就是目前的候选者
    for i in list1:
        if vote_num == 0:
            x = i  # 当票数为0时，我当班长
        if i == x:
            vote_num += 1
        else:
            vote_num -= 1
    print(x)

if __name__ == '__main__':
    # find_two()
    find_half()
