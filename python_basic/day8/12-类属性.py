# 作者: 王道 龙哥
# 2022年06月07日16时25分20秒
class Tool:
    """
    我是帮助
    """
    # count就是类属性
    count = 0

    def __init__(self, name):
        self.name = name
        # 针对类属性做一个计数+1
        Tool.count += 1

    @classmethod
    def show_tool_count(cls):
        """
        cls是类名，等价于Tool
        """
        print("工具对象的数量 %d" % cls.count)


# 创建工具对象
tool1 = Tool("斧头")
tool2 = Tool("榔头")
tool3 = Tool("铁锹")

print('总计实例化了 %d个工具对象' % Tool.count)

tool1.count = 99  # 给对象新增了一个count的属性
print(tool3.count)
# print(Tool.__dict__)
Tool.show_tool_count()


class Dog(object):

    @staticmethod
    def help():
        # 不访问实例属性/类属性
        print("这是一个养狗的说明文档")


# 通过类名.调用静态方法 - 不需要创建对象
Dog.help()
