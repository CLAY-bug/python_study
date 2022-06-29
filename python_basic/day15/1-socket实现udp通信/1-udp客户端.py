# 作者: 王道 龙哥
# 2022年06月15日10时27分51秒
import socket
import sys

# socket.AF_INET代表ipv4, socket.SOCK_DGRAM代表udp
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest_addr = ('192.168.1.35', 2000)
client.sendto('helloworld'.encode('utf8'), dest_addr)
recv_data = client.recvfrom(50)
print(recv_data[0].decode('utf8'))
client.close()
