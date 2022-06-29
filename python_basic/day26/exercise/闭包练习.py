# 作者 ： 赖鑫
# 2022年06月28日21时04分33秒

def counter(start=0):
    def incr():
        nonlocal start
        start += 1
        return start

    return incr


c1 = counter(5)  # 5传给start c1 = incr
print(c1())  # 调用incr()
print(c1())
