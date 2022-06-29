# 作者: 王道 龙哥
# 2022年06月14日15时02分31秒

class A:
    def __init__(self):
        self.name='xiongda'
    def sleep(self):
        print('sleep')

class B(A):
    def __init__(self):
        super().__init__()
        self.age=10

b=B()
b.sleep()
print(b.name)