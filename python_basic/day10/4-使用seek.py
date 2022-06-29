# 作者: 王道 龙哥
# 2022年06月09日11时50分45秒

import os


# seek的作用就是移动光标
def use_seek1():
    f = open('readme', 'r+', encoding='utf8')
    f.seek(6, os.SEEK_SET)  # 相对于开头偏移6个字节
    text = f.read()
    print(text)


def use_seek2():
    """
    偏移到结尾，从尾部接着写
    :return:
    """
    f = open('readme', 'r+', encoding='utf8')
    f.seek(0, os.SEEK_END)  # 偏移到文件尾部
    f.write('文件存数据')
    f.close()


if __name__ == '__main__':
    # use_seek1()
    use_seek2()
