# 作者: 王道 龙哥
# 2022年06月04日10时10分03秒
#num1和num2是形参
def sum_2_num(num1, num2):
    result = num1 + num2

    print("%d + %d = %d" % (num1, num2, result))


sum_2_num(50, 20)

#没有return，函数返回是None
def sum_3_num(num1, num2):
    """对两个数字的求和"""

    return num1 + num2

# 调用函数，并使用 result 变量接收计算结果
result = sum_3_num(10, 20)

print("计算结果是 %d" % result)

