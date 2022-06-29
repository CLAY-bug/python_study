# 作者 ： 赖鑫
# 2022年06月17日20时26分37秒


import socket
import sys
import struct

file_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
file_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
local_addr = ('192.168.1.35', 2000)
file_server.bind(local_addr)
file_server.listen(10)
client_socket, client_addr = file_server.accept()
print(client_addr)

# 要下载的文件名
file_name = "Readme"
# 先发文件的长度,以字节流计算长度
b_file_name = file_name.encode('utf8')
client_socket.send(struct.pack('I', len(b_file_name)))  # 发送文件名长度
client_socket.send(b_file_name)  # 文件名

file = open(file_name, 'rb')  # 打开文件
content_bytes = file.read()  # 读取文件内容
client_socket.send(struct.pack('I', len(content_bytes)))  # 发送文件内容长度
client_socket.send(content_bytes)  # 发送文件内容
file.close()  # 关闭文件
client_socket.close()  # 关闭服务器端套接字
file_server.close()
