# 作者 ： 赖鑫
# 2022年06月29日19时39分26秒

class Test:
    def __init__(self, func):
        print(f"my name is {func.__name__}")
        self.func = func

    def __call__(self, *args, **kwargs):
        print('this is test function')
        self.func()


@Test
def test():
    print("---test---")


test()  # 这是类的一个对象()
