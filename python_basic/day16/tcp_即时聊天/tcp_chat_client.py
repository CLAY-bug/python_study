# 作者 ： 赖鑫
# 2022年06月16日17时13分03秒

import socket
import select
import sys

tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 重用ip地址和端口
tcp_client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# 设置目的地址并请求连接
dest_addr = (sys.argv[1], 2000)
tcp_client.connect(dest_addr)

# 创建epoll对象
epoll = select.epoll()
# 指定socket监听指定的事件
epoll.register(sys.stdin.fileno(), select.EPOLLIN)  # 监听系统标准输入是否有数据
epoll.register(tcp_client.fileno(), select.EPOLLIN)  # 监听tcp客户端缓冲区

while True:
    events = epoll.poll(-1, 2)
    # fd 文件描述符   event 事件类型
    for fd, event in events:
        if fd == sys.stdin.fileno():  # 当标准输入里有数据
            send_data = input("请输入要发送的信息：")
            tcp_client.send(send_data.encode('utf8'))
        elif fd == tcp_client.fileno():  # 当接收缓冲区里有数据
            # 接收服务器发来的数据
            recv_data = tcp_client.recv(1024)
            if not recv_data:  # 当读到内容为空时
                print("服务器断开了！")
                exit()
            print(recv_data.decode('utf8'))
