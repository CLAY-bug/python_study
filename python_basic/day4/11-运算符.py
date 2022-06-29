# 作者: 王道 龙哥
# 2022年06月03日15时18分25秒
def calc():
    print(5 / 2)
    print(5 // 2)
    i = 100
    print(-i)


def relation():
    print(3 > 4)


def logic():
    print(5 and 3)  # and是遇假则假，都真返回后一个
    print(0 or 5)
    0 and print('you can see and')  # 短路操作，and前面为假，print不会得到执行
    0 or print('you can see or')


calc()
# relation()
# logic()
