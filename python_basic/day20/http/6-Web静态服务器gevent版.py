import socket
import re
import gevent
from gevent import monkey

monkey.patch_all()

#跟多进程多线程一致的
def service_client(new_socket):
    '''为客户端返回数据'''

    # 接收http请求
    request = new_socket.recv(1024).decode('utf-8')
    if request:
        request_lines = request.splitlines()
        print("")
        print(">" * 20)
        print(request_lines)

        file_name = ""
        ret = re.match(r"[^/]+(/[^ ]*)", request_lines[0])
        if ret:
            file_name = ret.group(1)
            if file_name == "/":
                file_name = "/index.html"
        print(file_name)
        try:
            f = open("./html" + file_name, "rb")
        except:
            response = "HTTP/1.1 404 NOT FOUND\r\n"
            response += "\r\n"
            response += "-------file not found-------"
            new_socket.send(response)
        else:
            html_content = f.read()
            f.close()
            response = "HTTP/1.1 200 OK\r\n"
            response += "\r\n"

            new_socket.send(response.encode('utf-8'))
            new_socket.send(html_content)
    new_socket.close()


def main():
    '''创建套接字'''
    # 初始化
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # 绑定
    tcp_server_socket.bind(("", 7890))

    # 激活
    tcp_server_socket.listen(128)

    while True:
        new_socket, socket_addr = tcp_server_socket.accept()
        gevent.spawn(service_client, new_socket)

    tcp_server_socket.close()


if __name__ == '__main__':
    main()
