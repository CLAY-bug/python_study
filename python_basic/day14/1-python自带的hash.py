# 作者: 王道 龙哥
# 2022年06月14日09时47分00秒
import hashlib

print(hash('longge'))  #hash里边加了盐值，每次进程结束后，下次启动盐值不一样
print(hash('longge'))