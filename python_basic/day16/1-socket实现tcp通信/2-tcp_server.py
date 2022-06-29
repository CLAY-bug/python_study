# 作者: 王道 龙哥
# 2022年06月16日10时10分21秒
from socket import *

# SOCK_STREAM代表tcp
tcp_server = socket(AF_INET, SOCK_STREAM)
server_addr = ('192.168.1.16', 2000)
tcp_server.bind(server_addr)
tcp_server.listen(10)  # tcp_server对象的缓冲大小
# 如果有新的客户端来链接服务器，那么就产生一个新的套接字专门为这个客户端服务
# client_socket用来为这个客户端服务
# tcp_server就可以省下来专门等待其他新客户端的链接
client_socket, client_addr = tcp_server.accept()
# 接收客户端的数据
recv_data = client_socket.recv(5)
print(recv_data)
recv_data = client_socket.recv(10)
print(recv_data)
client_socket.send(b'study')
client_socket.close()
tcp_server.close()
