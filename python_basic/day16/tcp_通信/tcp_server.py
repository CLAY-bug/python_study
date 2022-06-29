# 作者 ： 赖鑫
# 2022年06月16日17时23分41秒

import socket

tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 绑定地址
server_addr = ("192.168.1.35", 2000)
tcp_server.bind(server_addr)
# 把端口改为监听，被动连接,并等待客户端的连接请求
tcp_server.listen(10)
client_socket, client_addr = tcp_server.accept()
# 接受数据
recv_data = client_socket.recv(1024)
print(recv_data.decode('utf8'))
client_socket.send("我已收到信息！".encode('utf8'))

client_socket.close()
tcp_server.close()
