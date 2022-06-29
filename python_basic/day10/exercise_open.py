# 作者 ： 赖鑫
# 2022年06月13日22时05分30秒

def file_open():
    # 打开文件,返回文件对象
    file = open('readme', encoding='utf-8')
    # 读取文件内容，并把文件指针移动到文件的末尾
    text = file.read()
    print(text)
    file.close()


def file_read_write():
    file = open('readme', 'r+', encoding='utf8')
    file.write("this is my first write")
    # 因为写完文件之后会把文件指针移动到末尾
    # 接下来读文件从文件末尾开始读，所以读不到内容
    file.close()

def read_line():
    file = open('readme', 'r+', encoding='utf8')
    line_count = 0
    while True:
        text = file.readline()
        if not text:
            break
        print(text)
        line_count += 1
        print(f"一共有{line_count}行")
    file.close()




if __name__ == "__main__":
    # file_open()
    # file_read_write()
    read_line()