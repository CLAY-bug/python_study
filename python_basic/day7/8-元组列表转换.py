# 作者: 王道 龙哥
# 2022年06月06日11时28分29秒

info_tuple=(1,2,3)
info_tuple1=(1,2,3)
print(id(info_tuple))
print(id(info_tuple1))
info_list=list(info_tuple)
print(info_list)
info_tuple=tuple(info_list)
print(info_tuple)

print('-'*50)
#元组生成式,是需要加一个tuple
a=tuple(x if x % 2 == 0 else x ** 2 for x in range(10))
print(a)