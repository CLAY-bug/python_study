# 作者 ： 赖鑫
# 2022年06月28日21时50分29秒

def set_func(func):
    def verify():
        print("验证1----")
        print("验证2----")
        func()

    return verify


@set_func  # 调用装饰器，并把func()传给set_func函数并进行验证
def func1():
    print("功能1")


@set_func
def func2():
    print("功能2")


func1()
print("-" * 50)
func2()
