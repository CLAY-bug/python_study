# 作者: 王道 龙哥
# 2022年06月09日14时56分16秒

#图片，音乐，电影等非文本文件，必须是b模式
def open_b_read():
    f=open('readme', 'rb+')
    btext=f.read()
    print(btext)

def open_b_write():
    f=open('readme', 'rb+')
    # f.write(b'abc')
    f.write('烫').encode('utf8')
    f.close()

if __name__ == '__main__':
    open_b_write()