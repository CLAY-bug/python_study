# 作者: 王道 龙哥
# 2022年06月20日14时47分32秒
def gen():
    i = 0
    while i < 5:
        temp = yield i
        print(temp)
        i += 1


G = gen()
print(next(G))  # 第一次不可以传参
print(G.send('a'))
print(G.send('b'))
print(G.send('c'))
print(G.send('d'))
print(G.send('e'))
print(G.send('f'))
