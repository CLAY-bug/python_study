# 作者: 王道 龙哥
# 2022年06月20日14时36分55秒
def fib(n):
    current = 0
    num1, num2 = 0, 1
    while current < n:
        num = num1
        num1, num2 = num2, num1 + num2
        current += 1
        yield num
    return 'done'


F = fib(5)  # F是一个生成器对象
print(type(F))
# for i in F:
#     print(i)


while True:
    try:
        x = next(F)
        print("value:%d" % x)
    except StopIteration as e:
        print("生成器返回值:%s" % e.value)
        break
