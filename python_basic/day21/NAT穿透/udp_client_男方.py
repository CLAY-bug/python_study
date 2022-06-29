#!/usr/bin/python
# coding=utf-8

from socket import *
import select
import sys

# 1. 创建套接字
udp_socket = socket(AF_INET, SOCK_DGRAM)
# 注意 是元组，ip是字符串，端口是数字

# 2.这里是服务器的IP地址和端口
dest_addr = ('183.129.206.230', 9000)

# 3. 从键盘获取数据
send_data = input("请输入要发送的数据:")

# 4. 接收服务器发送过来女方的ip地址和端口
udp_socket.sendto(send_data.encode('utf-8'), dest_addr)

recv_data = udp_socket.recvfrom(1000)  #接的是女方的ip地址和端口
print(recv_data[0].decode('utf-8'))
# 5. #收到ip和端口后，进行分割
ip_port = recv_data[0].decode('utf-8').split()
ip_port[1] = int(ip_port[1])
ip_port=tuple(ip_port) #列表转元组
print(ip_port)
#给女方发一个world
udp_socket.sendto('world'.encode('utf-8'), ip_port)
recv_data=udp_socket.recvfrom(1024)
print(recv_data[0].decode('utf-8'))

#男方先说话
while True:
    input_data = input('请输入数据')
    udp_socket.sendto(input_data.encode('utf-8'), ip_port)
    recv_data = udp_socket.recvfrom(1024)
    print(recv_data[0].decode('utf-8'))
udp_socket.close()
