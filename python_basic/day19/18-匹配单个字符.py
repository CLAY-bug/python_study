# 作者: 王道 龙哥
# 2022年06月20日16时39分44秒
import re

ret = re.match(".", "M")
print(ret.group())

ret = re.match("t.o", "too")
print(ret.group())

ret = re.match("t.o", "two")
print(ret.group())

print('-' * 50)
# 使用[]
# 大小写h都可以的情况
ret = re.match("[hH]", "hello Python")
print(ret.group())
ret = re.match("[hH]", "Hello Python")
print(ret.group())
ret = re.match("[hH]ello Python", "Hello Python")
print(ret.group())

# 匹配0到9第一种写法
ret = re.match("[0123456789]Hello Python", "7Hello Python")
print(ret.group())

# 匹配0到9第二种写法
ret = re.match("[0-9]Hello Python", "7Hello Python")
print(ret.group())

ret = re.match("[0-35-9]Hello Python", "7Hello Python")
print(ret.group())

# 下面这个正则不能够匹配到数字4，因此ret为None
ret = re.match("[0-35-9]Hello Python", "4Hello Python")
if ret:
    print(ret.group())

print('-' * 50)
# 使用\d进行匹配
ret = re.match("嫦娥\d号", "嫦娥1号发射成功")
print(ret.group())

ret = re.match("嫦娥\d号", "嫦娥2号发射成功")
print(ret.group())

ret = re.match("嫦娥\d号", "嫦娥3号发射成功")
print(ret.group())

# 使用\s进行匹配
ret = re.match("嫦娥\s号", "嫦娥 号发射成功")
print(ret.group())

# 使用\w
ret = re.match("张\w", '张五爱学python')
print(ret.group())
