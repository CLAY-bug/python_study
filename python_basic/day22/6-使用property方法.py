# 作者: 王道 龙哥
# 2022年06月23日10时26分33秒
class Foo:
    """
    I am Foo
    """

    def get_bar(self):
        """
        I am a function
        :return:
        """
        return 'laowang'

    Bar = property(get_bar)


obj = Foo()
print(obj.Bar)

print(Foo.__doc__)  # 类的注释
print(obj.get_bar.__doc__)  # 方法的注释
