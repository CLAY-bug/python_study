# 作者: 王道 龙哥
# 2022年06月17日10时15分28秒
from socket import *
import select
import sys
tcp_client_socket = socket(AF_INET, SOCK_STREAM)

if len(sys.argv) !=2:
    print('./chat_client.py IP')
    exit(2)
# 本地IP地址和端口
address = (sys.argv[1], 2000)
name = input("请输入你的名字：")
# 连接服务器
tcp_client_socket.connect(address)

epoll = select.epoll()
epoll.register(tcp_client_socket.fileno(), select.EPOLLIN)
epoll.register(sys.stdin.fileno(), select.EPOLLIN)
while True:
    epoll_list = epoll.poll(-1,2)
    for fd, event in epoll_list:
        if fd == sys.stdin.fileno():
            try:#这里主要是ctrl+D后我们能够自己控制退出码
                input_data = input()
            except:
                print('I want go')
                tcp_client_socket.close()
                exit(2)
            input_data =name +":"+input_data
            tcp_client_socket.send(input_data.encode('utf-8'))
        if fd == tcp_client_socket.fileno():
            recv_data = tcp_client_socket.recv(1024)
            if not recv_data:
                exit(0)
            print(recv_data.decode('utf-8'))

tcp_client_socket.close()