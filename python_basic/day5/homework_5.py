# 作者 ： 赖鑫
# 2022年06月04日14时00分30秒

while True:
    a = 10
    break


def part_test():
    global a
    print(a)
    a = 200
    print(a)


part_test()