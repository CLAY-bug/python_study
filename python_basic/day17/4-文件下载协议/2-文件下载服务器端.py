# 作者: 王道 龙哥
# 2022年06月17日15时00分56秒


from socket import *
import select
import sys
import time
import struct

tcp_server_socket = socket(AF_INET, SOCK_STREAM)

# 重用对应地址和端口
tcp_server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

# 本地IP地址和端口
address = ('192.168.1.16', 2000)

tcp_server_socket.bind(address)
# 端口激活
tcp_server_socket.listen(100)

client_socket, clientAddr = tcp_server_socket.accept()
# 连上了
print(clientAddr)

# 发文件名
file_name = "Readme"
# 先发报文头--文件名的长度
b_file_name = file_name.encode('utf-8')
client_socket.send(struct.pack("I", len(b_file_name)))  # 发送文件名的长度
client_socket.send(b_file_name)  # 发文件名

# 发文件内容
file = open(file_name, "rb")
text_bytes = file.read()
client_socket.send(struct.pack("I", len(text_bytes)))  # 文件内容长度
client_socket.send(text_bytes)  # 文件内容
file.close()
time.sleep(5)
client_socket.close()
tcp_server_socket.close()
