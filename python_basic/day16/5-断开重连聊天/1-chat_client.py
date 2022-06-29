# 作者: 王道 龙哥
# 2022年06月16日10时00分51秒

from socket import *
import select
import sys

# SOCK_STREAM代表tcp
tcp_client = socket(AF_INET, SOCK_STREAM)
dest_addr = ('192.168.1.16', 2000)
tcp_client.connect(dest_addr)  # 连接服务器

epoll = select.epoll()
# 告诉epoll监控标准输入
epoll.register(sys.stdin.fileno(), select.EPOLLIN)
epoll.register(tcp_client.fileno(), select.EPOLLIN)

while True:
    events = epoll.poll(-1, 2)
    for fd, event in events:
        if fd == sys.stdin.fileno():  # 代表标准输入里边有数据
            data = input('请输入数据:')
            tcp_client.send(data.encode('utf8'))
        elif fd == tcp_client.fileno():  # 代表标准输入里边有数据
            # 接收客户端的数据
            recv_data = tcp_client.recv(100)
            if not recv_data:
                print('对方断开了')
                exit()
            print(recv_data.decode('utf8'))

tcp_client.close()
