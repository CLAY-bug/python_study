# 作者: 王道 龙哥
# 2022年06月08日11时21分10秒
def demo1():
    num=int(input("输入整数："))
    print('demo1:{}'.format(num))
    return num

def demo2():
    num=demo1()
    print('I am demo2')
    return num

# 利用异常的传递性，在主程序捕获异常
try:
    print('try{}'.format(demo2()))
except Exception as result:
    print("未知错误 %s" % result)