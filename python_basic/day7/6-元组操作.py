# 作者: 王道 龙哥
# 2022年06月06日11时19分44秒
# 元组中 只包含一个元素 时，需要 在元素后面添加逗号，不加逗号就是整型元素
info_tuple = (50,)
print(type(info_tuple))


info_tuple = ("zhangsan", 18, 1.75, "zhangsan")

# 1. 取值和取索引
print(info_tuple[0])
# 已经知道数据的内容，希望知道该数据在元组中的索引
print(info_tuple.index("zhangsan"))

# 2. 统计计数
print(info_tuple.count("zhangsan"))
# 统计元组中包含元素的个数
print(len(info_tuple))


# 元组遍历.py
info_tuple = ("zhangsan", 18, 1.75)

# 使用迭代遍历元组
for my_info in info_tuple:

    # 使用格式字符串拼接 my_info 这个变量不方便！不用加号
    # 因为元组中通常保存的数据类型是不同的！
    print(my_info)
# 格式化字符串.py
info_tuple = ("小明", 21, 1.85)

# 格式化字符串后面的 `()` 本质上就是元组
print("%s 年龄是 %d 身高是 %.2f" % info_tuple)

info_str = "%s 年龄是 %d 身高是 %.2f" % info_tuple

print(info_str)