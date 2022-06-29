# 作者: 王道 龙哥
# 2022年06月06日11时02分01秒
# 列表推导式：用来快速地生成列表。
# 好处：代码比较短
# 坏处：可读性差
#
# [元素表达式 if(条件)  else  for 变量 in 迭代对象 ]
# 简单使用

a = [x for x in range(10)]
print(a)
b = []
for x in range(10):
    b.append(x)
print(b)
print('-' * 50)
# 2个for循环
a = [j for i in range(10) for j in range(i)]
print(a)
print('-' * 50)
a = [[col * row for col in range(5)] for row in range(5)]
print(a)
print('-' * 50)
a = [j for x in a for j in x]  # 2维列表转1维列表
print(a)
print('-' * 50)
# 只有if时
a = [x for x in range(10) if x % 2 == 0]  # 将只会筛选偶数
print(a)

# if-else的三元表达式, 列表生成式中有if else需要写到for前面
a = [x if x % 2 == 0 else x ** 2 for x in range(10)]
print(a)

# python 类似C中的三目运算
a = 10
b = 50
max = a if a > b else b
print(max)
