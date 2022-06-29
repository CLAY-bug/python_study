# 作者 ： 赖鑫
# 2022年06月16日17时13分03秒

import socket

tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 设置目的地址并请求连接
dest_addr = ("192.168.1.35", 2000)
tcp_client.connect(dest_addr)

send_data = input("请输入要发送的信息：")
tcp_client.send(send_data.encode('utf8'))
recv_data = tcp_client.recv(1025)
print(recv_data.decode('utf8'))

tcp_client.close()
