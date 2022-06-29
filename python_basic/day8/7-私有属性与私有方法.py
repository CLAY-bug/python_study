# 作者: 王道 龙哥
# 2022年06月07日15时06分41秒
class Women:

    def __init__(self, name):

        self.name = name
        self._height=166
        # 不要问女生的年龄
        self.__age = 18

    def __secret(self):
        print("我的年龄是 %d" % self.__age)

    def boy_friend(self):
        self.__secret()


xiaomei=Women('小美')
xiaomei.boy_friend()

# print(xiaomei._Women__age)