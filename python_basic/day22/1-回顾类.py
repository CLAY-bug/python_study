# 作者: 王道 龙哥
# 2022年06月23日09时43分54秒
class Province:
    country = '中国'

    def __init__(self, name):
        self.name = name


taiwan = Province('台湾省')
print(taiwan.__class__)  #输出对象所属类
print(type(taiwan))
del taiwan.name
