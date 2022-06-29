# 作者 ： 赖鑫
# 2022年06月12日19时30分24秒

class Tool:
    count = 0

    def __init__(self, name):
        self.name = name
        # 每次实例化对象时都要调用初始化函数
        Tool.count += 1

    @classmethod
    def show_tool_count(cls):
        """显示工具对象的总数"""
        print(f"工具对象的总数{cls.count}")

    @staticmethod
    def help():
        print("this is a staticmethod")


tool1 = Tool("工具1")
tool2 = Tool("工具2")
tool3 = Tool("工具3")
Tool.show_tool_count()
Tool.help()

