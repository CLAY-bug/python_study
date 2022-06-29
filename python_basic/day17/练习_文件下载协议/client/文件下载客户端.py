# 作者 ： 赖鑫
# 2022年06月17日20时26分23秒

import socket
import struct

file_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest_addr = ('192.168.1.35', 2000)
file_client.connect(dest_addr)

# 接收文件名长度
file_name_len = file_client.recv(4)
file_name = file_client.recv(struct.unpack('I', file_name_len)[0])  # 接收文件名
print(file_name.decode('utf8'))

file = open(file_name.decode('utf8'), 'wb')
# 接收文件内容长度
content_len = file_client.recv(4)
# 接收文件内容
content_bytes = file_client.recv(struct.unpack('I', content_len)[0])
file.write(content_bytes)
file.close()
file_client.close()
