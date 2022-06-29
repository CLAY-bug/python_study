# 作者: 王道 龙哥
# 2022年06月09日11时32分59秒

def open_r_add():
    # 1. 打开 - 文件名需要注意大小写，默认以文本方式打开
    file = open('readme', 'r+', encoding='utf8')
    # 2.写
    file.write('帅')
    # 3.关闭
    file.close()


def open_w():
    # 1. 打开 - 文件存在，就清空，不存在，就创建
    f = open('readme', 'w', encoding='utf8')
    f.write("hello python！\n")
    f.write("今天天气真好")
    f.close()


def read_line():
    """
    一次读一行，读空文件
    :return:
    """
    f = open('readme', 'r+', encoding='utf8')
    while True:
        text = f.readline()

        # 判断是否读到内容
        if not text:
            break

        # 每读取一行的末尾已经有了一个 `\n`
        print(text, end='')


def open_a_read():
    f = open('readme', 'a+', encoding='utf8')
    text = f.read()
    print(text)
    f.close()


def open_a_write():
    f = open('readme', 'a+', encoding='utf8')
    f.write('\n学习是一个持续的过程')
    f.close()


if __name__ == '__main__':
    # open_r_add()
    # open_w()
    # read_line()
    # open_a_read()
    open_a_write()
