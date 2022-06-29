# 作者: 王道 龙哥
# 2022年06月23日10时21分04秒
class Goods:
    def __init__(self):
        self.original_price = 100
        self.discount = 0.8

    @property
    def price(self):
        return self.original_price * self.discount

    @price.setter
    def price(self, value):
        self.original_price = value

    @price.deleter
    def price(self):
        del self.original_price


gas = Goods()
print(gas.price)
gas.price = 200
print(gas.price)
del gas.price
