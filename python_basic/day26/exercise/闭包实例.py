# 作者 ： 赖鑫
# 2022年06月28日20时43分09秒

def line_conf(a, b):
    def line(x):  # 定义闭包
        return a * x + b

    return line


line_1 = line_conf(1, 2)  # a=1,b=2
line_2 = line_conf(4, 5)
print(line_1(5))  # x = 5
print(line_2(5))  # x= 5
