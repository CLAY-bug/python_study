# 作者 ： 赖鑫
# 2022年06月17日00时28分33秒

import socket
import select
import sys

tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 设置目的地址并请求连接服务器
dest_addr = (sys.argv[1], 2000)
name = input("请输入你的名字:")
tcp_client.connect(dest_addr)

# 创建epoll对象
epoll = select.epoll()
# 指定socket监听指定的事件
epoll.register(sys.stdin.fileno(), select.EPOLLIN)  # 监听系统标准输入是否有数据
epoll.register(tcp_client.fileno(), select.EPOLLIN)  # 监听tcp客户端缓冲区

while True:
    events = epoll.poll(-1, 10)
    # fd 文件描述符   event 事件类型
    for fd, event in events:
        if fd == sys.stdin.fileno():  # 当标准输入里有数据
            send_data = input("")
            input_data = name + ':' + send_data
            tcp_client.send(input_data.encode('utf8'))
        elif fd == tcp_client.fileno():  # 当接收缓冲区里有数据
            # 接收服务器发来的数据
            recv_data = tcp_client.recv(1024)
            print(recv_data.decode('utf8'))
            if not recv_data:  # 当读到内容为空时
                print("服务器断开了！")
                exit()
            print(recv_data.decode('utf8'))
