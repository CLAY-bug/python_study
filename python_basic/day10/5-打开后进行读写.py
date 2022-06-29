# 作者: 王道 龙哥
# 2022年06月09日14时41分17秒
import os


def write_read():
    # 打开文件并返回文件对象
    f = open('readme', 'r+', encoding='utf8')
    # 写数据
    f.write('world')
    # 刷新位置指针
    f.seek(0, os.SEEK_CUR)
    # 读数据
    text = f.read(6)
    print(text)
    f.close()


def read_write():
    # 打开文件并返回文件对象
    f = open('readme', 'r+', encoding='utf8')
    # 读数据
    text = f.read(6)
    print(text)
    # 刷新位置指针
    f.seek(0, os.SEEK_CUR)
    f.write('java')
    f.close()


if __name__ == '__main__':
    # write_read()
    read_write()
