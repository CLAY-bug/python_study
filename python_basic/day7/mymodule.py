# 作者: 王道 龙哥
# 2022年06月06日09时49分04秒

def demo1():
    print('I am module')


if __name__ == '__main__':
    name = 'xiaoming'  # 是全局变量，但是调用函数时，要传递给函数
    demo1()  # 这里是测试接口
