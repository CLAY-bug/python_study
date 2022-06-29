# 作者: 王道 龙哥
# 2022年06月23日10时04分38秒
class Goods:
    @property
    def price(self):
        print('@property')

    @price.setter
    def price(self,value):
        print('@price.setter')

    @price.deleter
    def price(self):
        print('@price.deleter')

obj=Goods()
obj.price # 自动执行 @property 修饰的 price 方法，并获取方法的返回
obj.price=123  #自动执行 @price.setter 修饰的 price 方法，并将  123 赋值给方法的参数
del obj.price  # 自动执行 @price.deleter 修饰的 price 方法
