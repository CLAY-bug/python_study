# 作者: 王道 龙哥
# 2022年06月17日15时04分18秒
from socket import *
import select
import sys
import time
import struct

tcp_client_socket = socket(AF_INET, SOCK_STREAM)

# 本地IP地址和端口
address = ('192.168.1.16', 2000)

# 连接服务器
tcp_client_socket.connect(address)

# 先接文件名
file_name_len = tcp_client_socket.recv(4)
file_name = tcp_client_socket.recv(struct.unpack('I', file_name_len)[0])  # 接到文件名

file = open(file_name.decode('utf8'), 'wb')
# 接文件内容长度
file_content_len = tcp_client_socket.recv(4)
# 接文件内容
file_content = tcp_client_socket.recv(struct.unpack('I', file_content_len)[0])
# 写进去
file.write(file_content)
file.close()
tcp_client_socket.close()