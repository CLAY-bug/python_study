# 作者 ： 赖鑫
# 2022年06月16日17时23分41秒

import socket
import select
import sys

tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 重用对应的ip地址和端口
tcp_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# 绑定地址
server_addr = (sys.argv[1], 2000)
tcp_server.bind(server_addr)
# 监听并设置最大连接数，并等待客户端的连接请求
tcp_server.listen(10)

# 创建epoll对象
epoll = select.epoll()
# 指定监听事件
epoll.register(sys.stdin.fileno(), select.EPOLLIN)  # 监听系统标准输入里是否有数据
epoll.register(tcp_server.fileno(), select.EPOLLIN)  # 监听是否有人连接服务器

client_socket = None
while True:
    events = epoll.poll(-1, 2)
    for fd, event in events:
        if fd == tcp_server.fileno():  # 当有客户端连接服务器时
            client_socket, client_addr = tcp_server.accept()
            epoll.register(client_socket.fileno(), select.EPOLLIN)  # 监听接收缓冲里是否有数据
        if fd == sys.stdin.fileno():  # 当标准输入里有数据时
            # 输入数据发给客户端
            data = input("请输入发给客户端的话：")
            client_socket.send(data.encode('utf8'))
        elif fd == client_socket.fileno():  # 当接收缓冲区里有数据时
            # 接受数据
            recv_data = client_socket.recv(1024)
            if not recv_data:  # 当读到内容为空时
                print("\n对方已下线！")
                # 当客户端断开时，关闭套接字，并继续监控下一个客户端连接
                epoll.unregister(client_socket.fileno())
                client_socket.close()
                continue
            print(recv_data.decode('utf8'))
