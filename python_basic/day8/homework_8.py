# 作者 ： 赖鑫
# 2022年06月11日22时57分26秒

# 单例模式：让类创建的对象，在系统中只有一个实例
class Printer:
    """这是一个打印机的类，一次只能打印一个东西"""
    # 定义变量用来记录单例对象引用
    instance = None

    def __new__(cls, *args, **kwargs):
        # 判读是否有实例存在，存在则直接返回，不存在就开辟空间返回对象引用
        if cls.instance is None:
            cls.instance = super().__new__(cls)
            return cls.instance
        else:
            return cls.instance

    def __init__(self, name):
        print(f"初始化实例，这是{name}")


# 实例化对象
print1 = Printer("打印数学试卷")
print(print1)
print2 = Printer("打印英语试卷")
print(print2)
# 可以发现两个实例的对象引用是一样的





