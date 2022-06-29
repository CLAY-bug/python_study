# 作者: 王道 龙哥
# 2022年06月20日16时48分11秒
import re

ret = re.match('[A-Z][a-z]*', "MM")
print(ret.group())

ret = re.match("[A-Z][a-z]*", "MnnM")
print(ret.group())

ret = re.match("[A-Z][a-z]*", "Aabcdef")
print(ret.group())

print('-' * 50)
# 练习+号
names = ["name1", "_name", "2_name", "__name__"]

for name in names:
    ret = re.match("[a-zA-Z_]+\w*", name)
    if ret:
        print("变量名 %s 符合要求" % ret.group())
    else:
        print("变量名 %s 非法" % name)

# 练习？号
# 需求：匹配出，0到99之间的数字
print('-' * 50)

ret = re.match("[1-9]?[0-9]", "7")
print(ret.group())

ret = re.match("[1-9]?\d", "33")
print(ret.group())

ret = re.match("[1-9]?\d", "09")
print(ret.group())  # \d匹配了0

# 匹配m，n
ret = re.match("[a-zA-Z0-9_]{6}", "12a3g45678")
print(ret.group())

ret = re.match("[a-zA-Z0-9_]{8,20}", "1ad12f23s34455ff66")
print(ret.group())

# 邮箱
email = 'luke1@163.com'

ret = re.match('[a-zA-Z0-9_]{4,20}@163.com', email)
print(ret.group())
