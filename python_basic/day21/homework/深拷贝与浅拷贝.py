# 作者 ： 赖鑫
# 2022年06月22日16时45分18秒

import copy

print('-----直接赋值------')
a = [1, 2, 3]
b = a  # 把a的引用赋给b，两个指向同一块内存
print(f'a的地址为:{id(a)},b的地址为{id(b)}')  # id一样
print(f'a改变前b={b}')
a[0] = 90
print(f'a改变后b={b}')  # a改变了，b也会改变

print('-----使用浅拷贝------')
a = [1, 2, 3]
b = copy.copy(a)  # 使用浅拷贝，开辟了一块新内存
print(f'a的地址为:{id(a)},b的地址为{id(b)}')  # id不一样
print(f'a改变前b={b}')
a[0] = 100
print(f'a改变后b={b}')  # a改变了并不会改变b
print('-' * 50)

print('-----二维列表使用浅拷贝------')
a = [1, 2, 3]
b = [4, 5, 6]
c = [a, b]  # 二维列表
d = copy.copy(c)
print(f'a的地址：{id(a)}')
print(f'c[0]的地址为：{id(c[0])}')  # c[0]地址等于a的地址
print(f'a改变前c={c}')
print(f'a改变前d={d}')
a[0] = 89
print(f'a改变后c={c}')  # a改变后，c也变了
print(f'a改变后d={d}')  # a改变后，d也变了

print('-----使用深拷贝------')
a = [1, 2, 3]
b = [4, 5, 6]
c = [a, b]  # 二维列表
d = copy.deepcopy(c)
print(f'a的地址：{id(a)}')
print(f'c[0]的地址为：{id(c[0])}')  # c[0]地址等于a的地址
print(f'a改变前c={c}')
print(f'a改变前d={d}')
a[0] = 89
print(f'a改变后c={c}')  # a改变后，c也变了
print(f'a改变后d={d}')  # a改变后，但是d没有变
