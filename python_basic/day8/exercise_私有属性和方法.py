# 作者 ： 赖鑫
# 2022年06月12日11时07分46秒

class Women:
    def __init__(self, name):
        self.name = name
        # 私有属性
        self.__age = 18

    def __secret(self):
        """私有方法"""
        print(f'我的年龄是{self.__age}')

    def boy_friend(self):
        self.__secret()


marry = Women("玛丽")
marry.boy_friend()
