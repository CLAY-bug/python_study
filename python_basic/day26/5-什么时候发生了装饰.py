# 作者: 王道 龙哥
# 2022年06月28日16时48分23秒
# 作者: 王道 龙哥
# 2022年06月28日16时43分06秒
def set_func(func):
    print('--开始进行装饰--')
    def call_func(*args,**kwargs):
        print('---权限验证---')
        func(*args,**kwargs)
    return call_func


@set_func
def test1(num):
    print("-----test1---- {}".format(num))

# test1=set_func(test1) #这就是@做的事情
test1(3)