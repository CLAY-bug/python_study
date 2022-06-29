# 作者 ： 赖鑫
# 2022年06月17日00时28分29秒

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
epoll.register(tcp_server.fileno(), select.EPOLLIN)  # 监听是否有人连接服务器
# 客户端列表，用来保存用户socket信息
client_list = []

while True:
    events = epoll.poll(-1, 10)
    for fd, event in events:
        if fd == tcp_server.fileno():  # 当有客户端连接服务器时
            # 将连接的用户添加到用户列表中，并进行监听
            client_socket, client_addr = tcp_server.accept()
            print(f'{client_addr}加入聊天室')
            client_list.append(client_socket)
            epoll.register(client_socket.fileno(), select.EPOLLIN)  # 监听接收缓冲里是否有数据

        for client in client_list:
            if fd == client.fileno():
                recv_data = client.recv(1024)  # 服务器不需要打印数据，只需要转发给其他客户
                if not recv_data:  # 当读到内容为空时
                    # 当客户端断开时，关闭套接字，并继续监控下一个客户端连接
                    epoll.unregister(client.fileno())
                    client_list.remove(client)
                    client.close()
                else:
                    for other_client in client_list:
                        if other_client is not client:
                            other_client.send(recv_data)
