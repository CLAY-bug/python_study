# 作者: 王道 龙哥
# 2022年06月09日11时19分00秒
# 1. 打开 - 文件名需要注意大小写，默认以文本方式打开
file = open('readme', encoding='utf8')
# 2.读取，
txt = file.read()
print(txt)
print('-' * 50)
txt = file.read()  # 读到文件尾，再读什么读不到
print(txt)
# 3.关闭
file.close()
