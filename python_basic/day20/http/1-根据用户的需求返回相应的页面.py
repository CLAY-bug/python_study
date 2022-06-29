import socket
import re


# 接收浏览器的请求，并给予响应
def service_client(new_socket):
    """为这个客户端返回数据"""

    # 1. 接收浏览器发送过来的请求 ，即http请求  
    # GET / HTTP/1.1
    # .....
    request = new_socket.recv(4096).decode("utf-8")
    # print(">>>"*50)
    print(request)  # 只有头部
    # 把头部进行剥离，得到头部的每一行
    request_lines = request.splitlines()
    print("")
    print(">" * 20)
    print(request_lines)
    if request_lines:
        # GET /index.html HTTP/1.1
        # get post put del
        file_name = ""
        # 使用正则表达式去处理第一行，为了得到请求的url
        # [^/]+ 不是斜杠一直吃，[^ ]*不是空格一直吃，(/[^ ]*)拿到的就是url
        ret = re.match(r"[^/]+(/[^ ]*)", request_lines[0])
        if ret:
            file_name = ret.group(1)
            print("*" * 50, file_name)
            if file_name == "/":
                file_name = "/index.html"

        # 2. 返回http格式的数据，给浏览器

        try:
            f = open("./html" + file_name, "rb")  # 打开请求的资源
        except:  # 如果没有就返回404
            response = "HTTP/1.1 404 NOT FOUND\r\n"
            response += "\r\n"
            response += "------file not found-----"
            new_socket.send(response.encode("utf-8"))
        else:
            html_content = f.read()  # 读取文件内容
            f.close()
            # 2.1 准备发送给浏览器的数据---header
            response = "HTTP/1.1 200 OK\r\n"
            response += "\r\n"
            # 2.2 准备发送给浏览器的数据---body
            # response += "hahahhah"

            # 将response header发送给浏览器
            new_socket.send(response.encode("utf-8"))
            # 将response body发送给浏览器
            new_socket.send(html_content)

    # 关闭套接
    new_socket.close()


def main():
    """用来完成整体的控制"""
    # 1. 创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 为了确保端口复用
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # 2. 绑定
    tcp_server_socket.bind(("192.168.1.35", 2000))

    # 3. 变为监听套接字
    tcp_server_socket.listen(128)

    while True:
        # 4. 等待新客户端的链接
        new_socket, client_addr = tcp_server_socket.accept()

        # 5. 为这个客户端服务
        service_client(new_socket)

    # 关闭监听套接字
    tcp_server_socket.close()


if __name__ == "__main__":
    main()
