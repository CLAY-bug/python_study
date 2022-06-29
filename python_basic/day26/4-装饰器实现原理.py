# 作者: 王道 龙哥
# 2022年06月28日16时43分06秒
def set_func(func):
    def call_func():
        print('---权限验证---')
        func()
    return call_func


@set_func
def test1():
    print("-----test1----")

# test1=set_func(test1) #这就是@做的事情
test1()