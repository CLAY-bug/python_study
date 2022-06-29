# 作者 ： 赖鑫
# 2022年06月23日20时09分57秒

from contextlib import contextmanager


@contextmanager
def file_open_system(file_path, file_mode):
    f = open(file_path, file_mode, encoding='utf8')  # 文件打开
    yield f  # 返回文件对象，并记住当前位置
    f.close()  # 文件关闭


with file_open_system('homework', 'r+') as f:
    print(f.read())
    f.write("人生苦短，我用python")
