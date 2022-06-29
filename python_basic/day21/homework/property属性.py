# 作者 ： 赖鑫
# 2022年06月22日23时10分24秒
class Good:
    def __init__(self):
        self.original_price = 100
        self.discount = 0.8

    @property
    def price(self):
        new_price = self.original_price * self.discount
        return new_price

    @price.setter
    def price(self, value):
        self.original_price = value

    @price.deleter
    def price(self):
        del self.original_price


obj = Good()
print(obj.price)
obj.price = 1000
del obj.price
