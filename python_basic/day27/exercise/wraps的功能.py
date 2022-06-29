# 作者 ： 赖鑫
# 2022年06月29日19时51分24秒

from functools import wraps


def set_func(func):
    @wraps(func)  # 通过添加wrap装饰，让函数显示自己的名字和注释
    def warpped_func(*args, **kwargs):
        """我是一个装饰器"""
        print('---start---')
        func(*args, **kwargs)
        print("---end---")

    return warpped_func


@set_func
def foo(num, *args, **kwargs):
    """我是普通函数"""
    print(f'num = {num}')


print(f'my name is {foo.__name__}\nmy doc is {foo.__doc__}')
