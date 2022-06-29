# 作者 ： 赖鑫
# 2022年06月15日10时36分27秒

import socket
import sys
# 创建udp_server服务器端套接字
udp_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 服务器一般会绑定端口
local_addr = (sys.argv[1], 2000)
udp_server.bind(local_addr)
# 等待客户端发送数据
recv_data = udp_server.recvfrom(1024)
print(recv_data[0].decode('utf8'))
recv_data = udp_server.recvfrom(1024)
print(recv_data[0].decode('utf8'))
print(recv_data[1])
# 给客户端返回一个信息
udp_server.sendto('hello client, i have receive message'.encode('utf8'), recv_data[1])
udp_server.close()
