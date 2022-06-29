# 作者: 王道 龙哥
# 2022年06月21日15时18分18秒
from socket import *
import select
import sys

# SOCK_STREAM代表tcp
tcp_server = socket(AF_INET, SOCK_STREAM)
server_addr = ('192.168.1.35', 2000)
tcp_server.bind(server_addr)
tcp_server.listen(10)  # tcp_server对象的缓冲大小
# 如果有新的客户端来链接服务器，那么就产生一个新的套接字专门为这个客户端服务
# client_socket用来为这个客户端服务
# tcp_server就可以省下来专门等待其他新客户端的链接
client_socket, client_addr = tcp_server.accept()
recv_data = client_socket.recv(1024)
print(recv_data.decode('utf8'))

# 响应是  响应头部+body
http_header = "HTTP/1.1 200 OK\r\n"
response = http_header + "\r\n"
response += 'Hello world'
client_socket.send(response.encode('utf8'))
client_socket.close()
tcp_server.close()
