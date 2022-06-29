# 作者 ： 赖鑫
# 2022年06月22日14时51分29秒

import socket

# 创建tcp套接字
tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 端口重用
tcp_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# 绑定本地ip和端口
local_addr = ("192.168.1.35", 2000)
tcp_server.bind(local_addr)
# 启动监听,等待连接
tcp_server.listen(10)
client_socket, client_addr = tcp_server.accept()
# 使用client_socket接收数据
recv_data = client_socket.recv(1024)
print(recv_data.decode('utf8'))

# 添加响应
http_header = "HTTP//1.1 200 ok\r\n"
response = http_header + "\r\n"
response += "hello lmx"
client_socket.send(response.encode('utf8'))
client_socket.close()
tcp_server.close()
