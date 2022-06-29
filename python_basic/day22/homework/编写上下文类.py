# 作者 ： 赖鑫
# 2022年06月23日20时18分05秒

class FileSystem:
    def __init__(self, file_path, file_mode):
        self.file_path = file_path
        self.file_mode = file_mode

    def __enter__(self):
        print("从这开始。。。")
        self.f = open(self.file_path, self.file_mode, encoding='utf8')  # 文件打开
        return self.f

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('从这里离开...')
        self.f.close()  # 文件关闭


with FileSystem('homework', 'r+') as f:
    print(f.read())
    f.write('人生苦短，我用python')
