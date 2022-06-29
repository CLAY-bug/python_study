# 作者 ： 赖鑫
# 2022年06月22日15时25分51秒
import re
import socket


def server_client(new_socket):
    """为客户端服务,并返回请求数据"""
    # 接收浏览器的http请求
    request = new_socket.recv(1024).decode('utf8')
    request_lines = request.splitlines()  # 分离头部内容，得到列表
    print("-" * 40)
    print(request_lines)
    if request_lines:
        file_name = ""
        # 使用正则表达式去处理第一行，为了得到请求的url
        ret = re.match(r'[^/]+(/[^ ]*)', request_lines[0])
        if ret:
            file_name = ret.group(1)  # 分组1，拿到的就是url
            print('The file name is >>>', file_name)
            if file_name == "/":
                file_name = "/index.html"  # 定位到首页
        try:
            f = open("./html" + file_name, "rb")  # 打开请求资源
        except:  # 如果没有就返回404
            response = "HTTP/1.1 404 NOT FOUND\r\n"
            response += "\r\n"
            response += "----file not found----"
            new_socket.send(response.encode('utf8'))
        else:
            html_content = f.read()  # 读取文件内容
            f.close()
            response = "HTTP/1.1 200 OK\r\n"
            response += "\r\n"
            new_socket.send(response.encode('utf8'))
            new_socket.send(html_content)
    new_socket.close()


def main():
    # 创建套接字
    tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 端口复用
    tcp_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # 绑定本地ip地址和端口
    local_addr = ("192.168.1.35", 2000)
    tcp_server.bind(local_addr)
    # 监听并等待连接
    tcp_server.listen(10)

    while True:
        # 等待新客户端连接，并分配套接字
        new_socket, client_addr = tcp_server.accept()
        # 为这个客户服务
        server_client(new_socket)

    tcp_server.close()


if __name__ == '__main__':
    main()
