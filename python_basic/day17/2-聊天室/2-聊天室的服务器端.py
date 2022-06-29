# 作者: 王道 龙哥
# 2022年06月17日10时15分37秒
from socket import *
import select
import sys

# SOCK_STREAM代表tcp
tcp_server = socket(AF_INET, SOCK_STREAM)

if len(sys.argv) != 2:
    print('./chat_client.py IP')
    exit(2)
# 本地IP地址和端口
server_addr = (sys.argv[1], 2000)

tcp_server.bind(server_addr)
tcp_server.listen(10)  # tcp_server对象的缓冲大小

epoll = select.epoll()
# epoll监控tcp_server
epoll.register(tcp_server.fileno(), select.EPOLLIN)

client_dict = {}

while True:
    epoll_events = epoll.poll()
    for fd, event in epoll_events:
        if fd == tcp_server.fileno():  # 代表有客户端连接
            client_socket, client_addr = tcp_server.accept()
            print("{} is coming".format(client_addr))
            epoll.register(client_socket.fileno(), select.EPOLLIN)  # 谁连上监控谁
            client_dict[client_socket.fileno()] = client_socket
        else:
            # 谁发过来了数据，读取对应客户端的数据
            recv_data = client_dict[fd].recv(1000)
            if recv_data:
                for fileno, client in client_dict.items():
                    if fd != fileno:#不给自己发，发给其他人
                        client.send(recv_data)
            else:  # 读对应的客户端拿到的是空，说明对应的客户端断开了
                # 先告诉epoll不监控了
                print('有客户端断开了')
                epoll.unregister(fd)
                client_dict[fd].close()
                client_dict.pop(fd)  # 从字典里删除
