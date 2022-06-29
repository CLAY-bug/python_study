# 作者 ： 赖鑫
# 2022年06月21日21时26分48秒
import re

s = 'hello world, now is 2020/7/20 18:48, 现在是2020年7月20日18时48分。'
com = re.compile(r'\d{4}/[01]?\d/[1-3]?\d\s(?:0\d|1\d|2[0-4])\:[0-5]\d')
ret = com.findall(s)
print(ret)
