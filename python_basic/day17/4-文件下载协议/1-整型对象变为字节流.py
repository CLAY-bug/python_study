# 作者: 王道 龙哥
# 2022年06月17日14时38分14秒
import struct
import os
import time

a = '我很帅你很牛'.encode('utf-8')
print(len(a))

len_bytes = struct.pack("I",len(a))
print(len_bytes)
print('length:', len(len_bytes))
b=struct.unpack('I',len_bytes)
print(b[0])
print(type(b[0]))

#网络中传输时，标准是要求都是大端
temp_big_bytes = struct.pack(">I", len(a))

print('length:', len(temp_big_bytes))
print(temp_big_bytes)
