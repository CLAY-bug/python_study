# 作者 ： 赖鑫
# 2022年07月01日19时06分16秒

from abc import abstractmethod, ABCMeta


class PayMent(metaclass=ABCMeta):
    """接口类"""

    @abstractmethod
    def pay(self, money):
        pass


class AliPay(PayMent):
    def pay(self, money):
        print(f'支付宝支付了{money}元')


class ApplePay(PayMent):
    def pay(self, money):
        print(f'苹果支付了{money}元')


def pay(pay_obj, money):
    pay_obj.pay(money)


# p = PayMent()

apple = ApplePay()
pay(apple, 200)
