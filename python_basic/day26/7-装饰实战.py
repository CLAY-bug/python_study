# 作者: 王道 龙哥
# 2022年06月28日17时01分03秒
# 定义函数：完成包裹数据
def makeBold(fn):
    def wrapped():
        return "<b>" + fn() + "</b>"
    return wrapped

# 定义函数：完成包裹数据
def makeItalic(fn):
    def wrapped():
        return "<i>" + fn() + "</i>"
    return wrapped

@makeBold
@makeItalic
def test3():
    return 'hello-world-3'

print(test3())