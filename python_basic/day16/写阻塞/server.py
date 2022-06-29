# 作者 ： 赖鑫
# 2022年06月17日14时22分25秒

import socket
import select
import sys

tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 重用地址和端口
tcp_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR)
# 服务器地址端口绑定并监听
local_addr = ('192.168.1.35', 2000)
tcp_server.bind(local_addr)
tcp_server.listen(10)
client_socket, client_addr = tcp_server.accept()

while True:
    pass
