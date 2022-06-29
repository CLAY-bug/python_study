# 作者: 王道 龙哥
# 2022年06月28日16时08分29秒

# 闭包来划线
def line_6(k, b):
    def create_y(x):
        print(k * x + b)

    return create_y


line_6_1 = line_6(1, 2)  # line_6_1是create_y闭包的入口地址
line_6_1(0)
line_6_1(1)
line_6_1(2)
line_6_2 = line_6(3, 5)
line_6_2(0)
line_6_2(1)
line_6_2(2)