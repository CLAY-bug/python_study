# 作者: 王道 龙哥
# 2022年06月17日11时35分44秒
from socket import *
import select
import sys

tcp_client_socket = socket(AF_INET, SOCK_STREAM)

# 本地IP地址和端口
address = ('192.168.1.16', 2000)

# 连接服务器
tcp_client_socket.connect(address)
temp_str = 'a' * 1000
total = 0
try:
    while True:
        #MSG_DONTWAIT的作用是不到1000个也可以发，发不了就可以去干别的事，不会卡主
        send_size = tcp_client_socket.send(temp_str.encode('utf-8'))
        total += send_size
        print(total)
        if send_size != 1000:
            print("peer close")
            exit(1)
except Exception as e:#try是防止崩溃的
    print(e)