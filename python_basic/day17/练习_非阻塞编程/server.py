# 作者 ： 赖鑫
# 2022年06月17日19时22分36秒

import socket
import sys

# 创建套接字、端口重用、地址绑定
tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
local_addr = ('192.168.1.35', 2000)
tcp_server.bind(local_addr)
# 端口激活
tcp_server.listen(10)
# 设置tcp_server非阻塞，没人连接时抛异常
tcp_server.setblocking(False)
client_socket = None

while True:
    try:
        client_socket, client_addr = tcp_server.accept()
    except Exception as e:
        pass
    if client_socket:
        # 设置client_socket为非阻塞，设置非阻塞时必须使用try，except来接收异常
        client_socket.setblocking(False)
        try:
            recv_data = client_socket.recv(1024)
            if not recv_data:
                print('拜拜')
                exit()
            print(recv_data.decode('utf8'))
        except Exception as e:
            pass
