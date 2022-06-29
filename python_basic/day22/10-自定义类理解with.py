# 作者: 王道 龙哥
# 2022年06月23日11时45分06秒
class File:
    def __init__(self, file_name, open_mode):
        self.file_name = file_name
        self.open_mode = open_mode

    def __enter__(self):  # 进入时调用
        """
        enter的返回值给as后的变量名
        :return:
        """
        self.f = open(self.file_name, self.open_mode, encoding='utf8')
        return self.f

    def __exit__(self, exc_type, exc_val, exc_tb):  # 退出时调用
        print('I will exit')
        self.f.close()


with File('file', 'w') as f:
    f.write('坚持练习，就是捷径')
