# 作者 ： 赖鑫
# 2022年06月17日19时22分30秒

import socket
import sys

tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest_addr = ('192.168.1.35', 2000)
tcp_client.connect(dest_addr)

while True:
    send_data = input("请输入要发给服务器的信息：")
    tcp_client.send(send_data.encode('utf8'))
tcp_client.close()
