# 作者 ： 赖鑫
# 2022年06月13日16时25分43秒

def demo1():
    return int(input("请输入一个整数："))


def demo2():
    return demo1()

try:
    print(demo2())
except Exception as e:
    print(e)
    print(e.__traceback__.tb_frame.f_globals["__file__"])