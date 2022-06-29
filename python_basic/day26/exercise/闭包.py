# 作者 ： 赖鑫
# 2022年06月28日20时14分37秒

def line(a, b):  # 这是函数
    def create_y(x):  # 在函数里定义函数，称为闭包
        print(a * x + b)

    return create_y


line_1 = line(1, 2)  # 返回的是create_y这个函数
line_1(3)  # 传递的值是给x的
line_1(4)
