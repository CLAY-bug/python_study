# 作者: 王道 龙哥
# 2022年06月06日15时19分06秒
num_str = "0123456789"

# 1. 截取从 2 ~ 5 位置 的字符串
print(num_str[2:6])

# 2. 截取从 2 ~ `末尾` 的字符串
print(num_str[2:])

# 3. 截取从 `开始` ~ 5 位置 的字符串
print(num_str[:6])

# 4. 截取完整的字符串
print(num_str[:])

# 5. 从开始位置，每隔一个字符截取字符串
print(num_str[::2])

# 6. 从索引 1 开始，每隔一个取一个
print(num_str[1::2])

print('-'*50)
# 倒序切片
# -1 表示倒数第一个字符
print(num_str[-1])

# 7. 拿倒数第二个
print(num_str[-2:-1])

# 8. 截取字符串末尾两个字符
print(num_str[-2:])

# 9. 字符串的逆序（面试题）
print(num_str[::-1])

print('-'*50)
for i in 'abcdefg':
    print(i)