# 作者 ： 赖鑫
# 2022年06月29日17时26分44秒

def time_func_args(pre='hello'):
    def time_func(func):
        def warpped_func():
            # 装饰器带有不同的参数会传入不同的值，不需要调用者再传值
            print(f'my name is {func.__name__}, pre = {pre}')
            return func()

        return warpped_func

    return time_func


@time_func_args('good')
def foo():
    print('i am foo')


@time_func_args("python")
def too():
    print("i am too")


foo()
too()
