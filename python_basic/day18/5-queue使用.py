# 作者: 王道 龙哥
# 2022年06月18日10时29分40秒
from multiprocessing import Queue

q = Queue(3)  # 初始化一个Queue对象，最多可接收三条put消息
q.put("消息1")
q.put("消息2")
print(q.full())  # False
q.put("消息3")
print(q.full())  # True

print(q.get())
print(q.get())
print(q.get())
