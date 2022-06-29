# 作者: 王道 龙哥
# 2022年06月23日14时33分44秒
from contextlib import contextmanager


@contextmanager
def my_open(path, mode):
    f = open(path, mode, encoding='utf8')
    yield f
    f.close()


with my_open('file', 'w') as f:
    f.write('心态不着急要自我肯定')
