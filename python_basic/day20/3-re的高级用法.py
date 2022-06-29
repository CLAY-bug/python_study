# 作者: 王道 龙哥
# 2022年06月21日10时58分50秒
import re

ret = re.search(r"\d+", "阅读次数为 9999")
print(type(ret))
print(ret.group())

ret = re.findall(r'\d+', "python = 9999, c = 7890, c++ = 12345")
print(ret)  # ret是列表，没有group方法

# 使用sub
ret = re.sub(r'\d+', '998', 'python 997')
print(type(ret))
print(ret)


def add(temp):
    str_num = temp.group()
    num = int(str_num) + 5
    return str(num)


ret = re.sub(r'\d+', add, 'python 997')
print(ret)

ret = re.sub(r'\d+', lambda x: str(int(x.group()) + 5), 'python 997')
print(ret)

# sub复杂的实战
s = 'hello world, now is 2020/7/20 18:48, 现在是2020年7月20日18时48分。'
ret_s = re.sub(r'年|月', r'/', s)
ret_s = re.sub(r'日', r' ', ret_s)
ret_s = re.sub(r'时', r':', ret_s)
ret_s = re.sub(r'分', r'', ret_s)
print(ret_s)

# findall 有问题,?:代表不让findall支取分组内内容
com = re.compile(r'\d{4}/[01]?\d/[1-3]?\d\s(?:0\d|1\d|2[0-4])\:[0-5]\d')
ret = com.findall(ret_s)
print(ret)
