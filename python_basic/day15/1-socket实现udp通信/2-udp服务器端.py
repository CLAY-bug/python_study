# 作者: 王道 龙哥
# 2022年06月15日10时28分00秒
from socket import *
import sys
# 1. 创建套接字
udp_server = socket(AF_INET, SOCK_DGRAM)

# 2. 绑定本地的相关信息，如果一个网络程序不绑定，则系统会随机分配
local_addr = (sys.argv[1], 2000) #  ip地址和端口号，ip一般不用写，表示本机的任何一个ip
udp_server.bind(local_addr)

# 3. 等待接收对方发送的数据,1024表示本次接收的最大字节数
recv_data=udp_server.recvfrom(5)
# 4. 显示接收到的数据
print(recv_data[0].decode('utf8'))
#这里是对方的ip地址和端口号
print(recv_data[1])
# 5. 给客户端发一个world
udp_server.sendto('Ilovepython'.encode('utf8'),recv_data[1])
udp_server.close()