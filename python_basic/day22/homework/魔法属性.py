# 作者 ： 赖鑫
# 2022年06月23日19时38分11秒

class Exercise:
    """这是我的说明文档"""

    def __init__(self):
        self.name = 'China'

    def __str__(self):
        return "china"

    def __del__(self):
        """重写del方法，在销毁对象之前打印日志"""
        print("对象即将被销毁")

    def __call__(self, *args, **kwargs):
        print("i am __call__")  # 对象名()直接调用


if __name__ == '__main__':
    print(Exercise.__doc__)  # 查看注释
    print(Exercise.__module__)
    exercise = Exercise()  # 实例化对象
    print(exercise.__class__)  # 查看对象所属的类
    exercise()
    print(exercise.__dict__)  # 查看对象中的所有属性
    print(Exercise.__dict__)  # 查看类中的所有属性
    print(exercise)
    del exercise  # 手动销毁对象
