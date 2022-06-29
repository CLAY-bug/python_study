# 作者: 王道 龙哥
# 2022年06月16日10时10分21秒
from socket import *
import select
import sys

# SOCK_STREAM代表tcp
tcp_server = socket(AF_INET, SOCK_STREAM)
server_addr = ('192.168.1.16', 2000)
tcp_server.bind(server_addr)
tcp_server.listen(10)  # tcp_server对象的缓冲大小
# 如果有新的客户端来链接服务器，那么就产生一个新的套接字专门为这个客户端服务
# client_socket用来为这个客户端服务
# tcp_server就可以省下来专门等待其他新客户端的链接
client_socket, client_addr = tcp_server.accept()

epoll = select.epoll()
# 告诉epoll监控标准输入
epoll.register(sys.stdin.fileno(), select.EPOLLIN)
epoll.register(client_socket.fileno(), select.EPOLLIN)

while True:
    events = epoll.poll(-1, 2)
    for fd, event in events:
        if fd == sys.stdin.fileno():  # 代表标准输入里边有数据
            data = input('请输入数据:')
            client_socket.send(data.encode('utf8'))
        elif fd == client_socket.fileno():  # 代表接收缓冲区里边有数据
            # 接收客户端的数据
            recv_data = client_socket.recv(100)
            if not recv_data:
                print('对方断开了')
                exit()
            print(recv_data.decode('utf8'))

client_socket.close()
tcp_server.close()
