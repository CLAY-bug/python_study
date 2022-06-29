# 作者: 王道 龙哥
# 2022年06月21日11时44分55秒
import re

ret = re.match(r'a', 'A', re.I)  # 不区分大小写
print(ret.group())

ret = re.match(r'.bc', '\nbc', re.S)
print(ret.group())
