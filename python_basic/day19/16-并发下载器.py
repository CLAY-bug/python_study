
# 作者: 王道 龙哥
# 2022年06月20日15时30分25秒
from gevent import monkey
monkey.patch_all()
import gevent
import random
import time
import requests  #requests已经替代了urllib了
 #放在代码最前面

def coroutine_work(url):
    print('GET: %s' % url)
    response = requests.get(url)
    data = response.text
    print('%d bytes received from %s.' % (len(data), url))

start=time.time()
# gevent.joinall([
#         gevent.spawn(coroutine_work, "http://www.baidu.com/"),
#         gevent.spawn(coroutine_work, "http://www.cskaoyan.com/"),
#         gevent.spawn(coroutine_work, "http://www.qq.com/")
# ])
# coroutine_work("http://www.baidu.com/")
# coroutine_work("http://www.cskaoyan.com/")
# coroutine_work("http://www.qq.com/")
end=time.time()
print(end-start)