# 作者: 王道 龙哥
# 2022年06月07日10时19分28秒
import sys
sys.setrecursionlimit(10000)
# 非必要情况下不要调试递归函数
def sum_numbers(num):
    print(num)

    # 递归的出口很重要，否则会出现死循环
    if num == 1:
        return

    sum_numbers(num - 1)


sum_numbers(3)
print('-' * 50)


def f(n):
    # 结束条件要写到return之前
    if 1 == n:
        return 1
    return n + f(n - 1)

print(f(1000))

print('-' * 50)

#上台阶
# 如果有n个台阶，每次只能走1个，或者2个台阶，到第n个台阶有多少种走法？
# s(n)=s(n-1)+s(n-2)

def step(n):
    if 1==n or 2==n:
        return n
    return step(n-1)+step(n-2)

print(step(4))