# 作者 ： 赖鑫
# 2022年06月22日19时54分35秒

class App:
    def __init__(self, name, version, docs):
        self.name = name
        self.version = version
        self.docs = docs

    def __str__(self):
        return f'{self.name}当前版本为：{self.version}'

    def install(self):
        """软件安装"""
        print(f'--->>>正在安装{self.name}\n下载完成')


class MiniOs:
    """MiniOs操作系统"""

    def __init__(self, name):
        self.name = name
        self.apps = []  # 软件列表

    def __str__(self):
        """
        重写str方法，返回自定义字符串
        :return:
        """
        return f"这是{self.name},已有的软件为：{self.apps}"

    def install(self, app: App):
        """
        安装软件
        :return:
        """
        if app.name in self.apps:
            print(f'{app.name}已经安装，无需重复安装')
        else:
            app.install()
            self.apps.append(app.name)  # 将软件加入列表


class QQ(App):
    """QQ继承APP类"""

    def install(self):
        """重写insatll方法"""
        print("正在解压QQ...")
        super().install()  # 调用父类的方法


class Safari(App):
    """浏览器继承App"""
    pass  # 不用重写，直接继承父类的方法


ubuntu = MiniOs('linux')
qq = QQ("qq", "10.5", "聊天软件")
safari = Safari("safari", "12.5", "浏览器")
ubuntu.install(qq)  # 下载qq
ubuntu.install(safari)  # 下载safari
ubuntu.install(safari)  # safari已经安装，无需重复安装
print(ubuntu)  # 因为重写了__str__方法，所以返回了自定义字符串
