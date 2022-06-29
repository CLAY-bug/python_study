# 作者 ： 赖鑫
# 2022年06月22日21时48分23秒
import re
import socket
from multiprocessing import Process


def client_server(new_socket):
    """为新客户端服务"""
    # 获取客户端的请求
    request_data = new_socket.recv(1024).decode('utf8')
    # 剥离请求头，并获取请求的url
    request_line = request_data.splitlines()
    if request_line:
        file_name = ''
        ret = re.match(r"[^/]+(/[^ ]*)", request_line[0])  # 请求头的第一行就是url
        if ret:
            file_name = ret.group(1)  # 用正则拿到url
            if file_name == '/':
                file_name = "/index.html"  # 默认去首页

        try:
            file = open('./html' + file_name, "rb")  # 以二进制打开html文件
        except:  # 找不到文件时
            response = "HTTP/1.1 404 NOT FOUND\r\n"  # response header，没有找到返回404
            response += "\r\n"
            response += "------file not found-----"  # response body
            new_socket.send(response.encode("utf-8"))  # 非客户端返回连接错误信息
        else:
            html_content = file.read()  # 读取html文件内容，也就是response body
            file.close()
            response = "HTTP/1.1 200 OK\r\n"  # 连接成功，返回状态码200
            response += "\r\n"

            new_socket.send(response.encode("utf-8"))  # 发送resonse header
            new_socket.send(html_content)  # 发送response body
    new_socket.close()


def main():
    tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    local_addr = ('192.168.1.35', 2000)
    tcp_server.bind(local_addr)
    tcp_server.listen(10)
    while True:
        new_socket, socket_addr = tcp_server.accept()
        # 为客户服务
        p = Process(target=client_server, args=(new_socket,))  # 为新连接的客户端创建一个新进程
        p.start()  # 进程开始

        new_socket.close()

    tcp_server.close()


if __name__ == '__main__':
    main()
