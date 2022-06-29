#!/usr/bin/python
# coding=utf-8

from socket import *

# 1. 创建套接字
udp_socket = socket(AF_INET, SOCK_DGRAM)

# 2. 绑定本地的相关信息，需要使用阿里云的内网地址
local_addr = ('172.20.34.17', 8080)  # ip地址和端口号，ip一般不用写，表示本机的任何一个ip
udp_socket.bind(local_addr)

# 3. 等待接收对方发送的数据
recv_boy_data = udp_socket.recvfrom(1024)  # 1024表示本次接收的最大字节数

# 4. 显示接收到的数据
print(recv_boy_data[0].decode('utf-8'))
print(recv_boy_data[1])

# # 这是你女朋友发过来的请求
recv_girl_data = udp_socket.recvfrom(1024)  # 1024表示本次接收的最大字节数
print(recv_girl_data[0].decode('utf-8'))
print(recv_girl_data[1])

# 给你女朋友发你的ip地址和端口
udp_socket.sendto((recv_boy_data[1][0] + " " + str(recv_boy_data[1][1])).encode('utf-8'), recv_girl_data[1])

# 给boy发他女朋友的ip地址和端口
udp_socket.sendto((recv_girl_data[1][0] + " " + str(recv_girl_data[1][1])).encode('utf-8'), recv_boy_data[1])
udp_socket.close()
