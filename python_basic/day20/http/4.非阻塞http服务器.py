#!/usr/bin/python
# author luke

import time
import socket
import sys
import re


class WSGIServer(object):
    """定义一个WSGI服务器的类"""

    def __init__(self, port, documents_root):

        # 1. 创建套接字
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 2. 绑定本地信息
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind(("", port))
        # 3. 变为监听套接字
        self.server_socket.listen(128)

        self.server_socket.setblocking(False)
        self.client_socket_list = list()

        self.documents_root = documents_root

    def run_forever(self):
        """运行服务器"""

        # 等待对方链接
        while True:

            # time.sleep(0.5)  # for test
            #下面try的目的是接收请求并放入列表
            try:
                new_socket, new_addr = self.server_socket.accept()
            except Exception as ret:
                # print("-----1----", ret)  # for test
                pass
            else:
                print(time.time())
                new_socket.setblocking(False)
                self.client_socket_list.append(new_socket)
            #遍历列表中的连接，如果有浏览器发过来数据，那么就处理
            for client_socket in self.client_socket_list:
                try:
                    request = client_socket.recv(4096).decode('utf-8')
                except Exception as ret:
                    # print("------2----", ret)  # for test
                    pass
                else:
                    if request:#有数据就处理数据
                        self.deal_with_request(request, client_socket)
                    else:#浏览器断开了
                        client_socket.close()
                        self.client_socket_list.remove(client_socket)
                        print(time.time())

            # print(self.client_socket_list)


    def deal_with_request(self, request, client_socket):
        """为这个浏览器服务器"""
        if not request:
            return

        request_lines = request.splitlines()
        #这个for循环是为了打印看数据
        for i, line in enumerate(request_lines):
            print(i, line)

        # 提取请求的文件(index.html)
        # GET /a/b/c/d/e/index.html HTTP/1.1
        ret = re.match(r"([^/]*)([^ ]+)", request_lines[0])
        if ret:
            print("正则提取数据:", ret.group(1))
            print("正则提取数据:", ret.group(2))
            file_name = ret.group(2)
            if file_name == "/":
                file_name = "/index.html"


        # 读取文件数据
        try:
            f = open(self.documents_root+file_name, "rb")
        except:
            response_body = "file not found, 请输入正确的url"
            response_header = "HTTP/1.1 404 not found\r\n"
            response_header += "Content-Type: text/html; charset=utf-8\r\n"
            response_header += "Content-Length: %d\r\n" % (len(response_body))
            response_header += "\r\n"

            # 将header返回给浏览器
            client_socket.send(response_header.encode('utf-8'))

            # 将body返回给浏览器
            client_socket.send(response_body.encode("utf-8"))
        else:
            content = f.read()
            f.close()

            response_body = content
            response_header = "HTTP/1.1 200 OK\r\n"
            response_header += "Content-Length: %d\r\n" % (len(response_body))
            response_header += "\r\n"

            # 将header返回给浏览器
            client_socket.send( response_header.encode('utf-8') + response_body)


# 设置服务器服务静态资源时的路径
DOCUMENTS_ROOT = "./html"


def main():
    """控制web服务器整体"""
    # python3 xxxx.py 7890
    if len(sys.argv) == 2:
        port = sys.argv[1]
        if port.isdigit():
            port = int(port)
    else:
        print("运行方式如: python3 xxx.py 7890")
        return

    print("http服务器使用的port:%s" % port)
    http_server = WSGIServer(port, DOCUMENTS_ROOT)
    http_server.run_forever()


if __name__ == "__main__":
    main()