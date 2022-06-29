# 作者: 王道 龙哥
# 2022年06月04日11时17分29秒

#可变类型的特点，就是
demo_list = [1, 2, 3]
print(demo_list)
print("定义列表后的内存地址 %d" % id(demo_list))

demo_list.append(999)
print(demo_list)
demo_list.pop(0)  #删除0位置的元素
print(demo_list)
demo_list.remove(2) #删除值为2的元素
print(demo_list)
demo_list[0] = 10
print(demo_list)

print("修改列表数据后的内存地址 %d" % id(demo_list))

