#!/usr/bin/python
# coding=utf-8

from socket import *
import select
import sys

# 1. 创建套接字
udp_socket = socket(AF_INET, SOCK_DGRAM)
# 注意 是元组，ip是字符串，端口是数字

# 2.这里是服务器的IP地址和端口
dest_addr = ('47.115.45.50', 8000)

# 3. 从键盘获取数据
send_data = input("请输入要发送的数据:")

# 4. 发送数据到指定的电脑上的指定程序中
udp_socket.sendto(send_data.encode('utf-8'), dest_addr)

recv_data = udp_socket.recvfrom(1000)
print(recv_data[0].decode('utf-8'))
# 5. 关闭套接字

ip_port = recv_data[0].decode('utf-8').split()
ip_port[1] = int(ip_port[1])
print(ip_port)

epoll = select.epoll()
# select.EPOLLIN如果缓冲区里有数据，就可读
epoll.register(udp_socket.fileno(), select.EPOLLIN)
epoll.register(sys.stdin.fileno(), select.EPOLLIN)

while True:
    epoll_list = epoll.poll()
    # print(epoll_list)
    for fd, event in epoll_list:
        if fd == sys.stdin.fileno():
            try:
                input_data = input()
            except:
                print('I want go')
                exit(0)
            udp_socket.sendto(input_data.encode('utf-8'), ip_port)
        if fd == udp_socket.fileno():
            recv_data = udp_socket.recvfrom(1024)
            print(recv_data[0].decode('utf-8'))

udp_socket.close()
