# 作者: 王道 龙哥
# 2022年06月16日10时00分51秒

from socket import *

#SOCK_STREAM代表tcp
tcp_client=socket(AF_INET,SOCK_STREAM)
dest_addr=('192.168.1.16',2000)
tcp_client.connect(dest_addr)  #连接服务器
#发送数据
tcp_client.send(b'python6 duyan')
tcp_client.close()
