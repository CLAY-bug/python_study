# 作者 ： 赖鑫
# 2022年06月15日10时36分19秒

import socket
# 创建UDP的套接字
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest_addr = ('192.168.1.35', 2000)
# 给服务器端发送数据
client.sendto('hello server'.encode('utf8'), dest_addr)
client.sendto('second send'.encode('utf8'), dest_addr)
# 客户端接受数据
recv_data = client.recvfrom(1024)
print(f"{recv_data[0].decode('utf8')}")
print(recv_data[1])
client.close()

