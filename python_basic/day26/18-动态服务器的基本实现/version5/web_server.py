#!/usr/bin/python
# author luke

import socket
import re
import multiprocessing
import time


class WSGIServer(object):
    def __init__(self, port, documents_root, app):
        # 1. 创建套接字
        self.tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # 2. 绑定
        self.tcp_server_socket.bind(("", port))

        # 3. 变为监听套接字
        self.tcp_server_socket.listen(128)

        # 设定资源文件的路径
        self.documents_root = documents_root

        # 设定web框架（django）可以调用的函数(对象)
        self.app = app

    def service_client(self, new_socket):
        """为这个客户端返回数据"""

        # 1. 接收浏览器发送过来的请求 ，即http请求
        # GET / HTTP/1.1
        # .....
        request = new_socket.recv(1024).decode("utf-8")
        # print(">>>"*50)
        # print(request)

        request_lines = request.splitlines()
        print("")
        print(">" * 20)
        print(request_lines)

        # GET /index.html HTTP/1.1
        # get post put del
        file_name = ""
        ret = re.match(r"[^/]+(/[^ ]*)", request_lines[0])
        if ret:
            file_name = ret.group(1)
            # print("*"*50, file_name)
            if file_name == "/":
                file_name = "/index.html"

        # 2. 返回http格式的数据，给浏览器
        if not file_name.endswith(".py"):
            try:
                # 针对访问的请求后缀是css，后缀是js静态文件进行加载
                f = open(self.documents_root + file_name, "rb")
            except:
                response = "HTTP/1.1 404 NOT FOUND\r\n"
                response += "\r\n"
                response += "------file not found-----"
                new_socket.send(response.encode("utf-8"))
            else:
                html_content = f.read()
                f.close()
                # 2.1 准备发送给浏览器的数据---header
                response = "HTTP/1.1 200 OK\r\n"
                response += "\r\n"
                # 2.2 准备发送给浏览器的数据---boy
                # response += "hahahhah"

                # 将response header发送给浏览器
                new_socket.send(response.encode("utf-8"))
                # 将response body发送给浏览器
                new_socket.send(html_content)
        else:
            # 2.2 如果是以.py结尾，那么就认为是动态资源的请求
            env = dict()
            # 浏览器请求的url添加到env中
            env['PATH_INFO'] = file_name
            # 传入回调函数给application
            body = self.app(env, self.set_response_header)
            # 解析头部
            header = "HTTP/1.1 %s\r\n" % self.status
            header += "Content-Type: text/html; charset=utf-8\r\n"
            # Content-Length是编码后的字节流的长度
            header += "Content-Length: %d\r\n" % len(body.encode("utf-8"))
            # 解析头部
            for temp in self.headers:
                header += "%s:%s\r\n" % (temp[0], temp[1])

            header += "\r\n"
            response = header + body
            # 发送response给浏览器
            new_socket.send(response.encode("utf-8"))

        # 关闭套接
        new_socket.close()

    def run_forever(self):
        """用来完成整体的控制"""

        while True:
            # 4. 等待新客户端的链接
            new_socket, client_addr = self.tcp_server_socket.accept()

            # 5. 为这个客户端服务
            p = multiprocessing.Process(target=self.service_client, args=(new_socket,))
            p.start()

            new_socket.close()

        # 关闭监听套接字
        self.tcp_server_socket.close()

    def set_response_header(self, status, headers):
        self.status = status
        # web服务器想告诉浏览器附加头部是多少
        self.headers = [("server", "mini_web v8.8")]
        self.headers += headers


import sys


def main():
    """控制整体，创建一个web 服务器对象，然后调用这个对象的run_forever方法运行"""
    """控制web服务器整体"""
    # python3 xxxx.py 7890
    if len(sys.argv) == 3:
        # 获取web服务器的port
        port = sys.argv[1]
        if port.isdigit():
            port = int(port)
        # 获取web服务器需要动态资源时，访问的web框架名字
        web_frame_module_app_name = sys.argv[2]
    else:
        print("运行方式如: python3 xxx.py 7890 my_web_frame_name:application")
        return

    # 如何读取配置文件，通过eval把字符串变为字典
    with open("./web_server.conf") as f:
        conf_info = eval(f.read())
    # 设置静态资源访问的路径
    g_static_document_root = conf_info['static_path']
    # 设置动态资源访问的路径
    g_dynamic_document_root = conf_info['dynamic_path']
    # 将动态路径即存放py文件的路径，添加到path中，这样python就能够找到这个路径了
    sys.path.append(g_dynamic_document_root)

    ret = re.match(r"([^:]*):(.*)", web_frame_module_app_name)
    if ret:
        # 获取模块名
        web_frame_module_name = ret.group(1)
        # 获取可以调用web框架的应用名称
        app_name = ret.group(2)

    # 导入web框架的主模块
    web_frame_module = __import__(web_frame_module_name)
    # 获取那个可以直接调用的函数(对象)
    app = getattr(web_frame_module, app_name)

    print("http服务器使用的port:%s" % port)
    wsgi_server = WSGIServer(port, g_static_document_root, app)
    wsgi_server.run_forever()


if __name__ == "__main__":
    main()
