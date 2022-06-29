# 作者: 王道 龙哥
# 2022年06月06日10时26分40秒
name_list = ["zhangsan", "lisi", "wangwu", "wangxiaoer"]
num_list = [6, 8, 4, 1, 10]

# 逆序（反转）
name_list.reverse()
num_list.reverse()

print(name_list)
print(num_list)
print('-'*50)
# 升序
name_list.sort()
num_list.sort()
print(name_list)
print(num_list)
# 降序
print('-'*50)
name_list.sort(reverse=True)
num_list.sort(reverse=True)
print(name_list)
print(num_list)

# 使用迭代遍历列表
for my_name in name_list:

    print("我的名字叫　%s" % my_name)