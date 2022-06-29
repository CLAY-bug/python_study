# 作者: 王道 龙哥
# 2022年06月04日11时50分35秒

num = 10


def demo():
    global num  #如果要在函数内修改全局变量值，就必须加global 拿过来
    num = 5
    print('demo里的num %d' % num)


demo()
print(num)
