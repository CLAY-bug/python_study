# 作者: 王道 龙哥
# 2022年06月06日15时29分38秒
fruits = {"apple", "banana", "cherry"}
fruits.add("apple")
print(fruits)
print(id(fruits))
x = fruits.copy()
print(id(x))  #copy后地址不一样了
print(x)

a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)