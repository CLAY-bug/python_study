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

epoll = select.epoll()
# 告诉epoll监控标准输入
epoll.register(sys.stdin.fileno(), select.EPOLLIN)
epoll.register(tcp_server.fileno(), select.EPOLLIN)

client_socket = None
while True:
    events = epoll.poll(-1, 3)
    for fd, event in events:
        if fd == tcp_server.fileno():
            # 客户端有人连接我
            client_socket, _ = tcp_server.accept()
            epoll.register(client_socket.fileno(), select.EPOLLIN)
        elif fd == sys.stdin.fileno():  # 代表标准输入里边有数据
            data = input('请输入数据:')
            if not client_socket:
                print('客户端没来连')
                continue
            client_socket.send(data.encode('utf8'))
        elif fd == client_socket.fileno():  # 代表标准输入里边有数据
            # 接收客户端的数据
            recv_data = client_socket.recv(100)
            if not recv_data:
                print('对方断开了')
                # 客户端断开后，不让小弟监控了
                epoll.unregister(client_socket.fileno())
                client_socket.close()
                continue
            print(recv_data.decode('utf8'))

client_socket.close()
tcp_server.close()
