# 作者: 王道 龙哥
# 2022年06月23日11时00分34秒
class Person:
    def __init__(self):
        self.name='laowang'

if __name__ == '__main__':

    print(Person.__module__)

    print(__name__) #当前模块调用输出是__main__，其他模块调用该模块得到的是本文件名