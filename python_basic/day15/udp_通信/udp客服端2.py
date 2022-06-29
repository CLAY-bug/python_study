# 作者 ： 赖鑫
# 2022年06月15日19时45分10秒

import socket

# 创建套接字
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 设置目的地址
dest_ip = input("请输入目的ip：")
dest_port = int(input("请输入目的端口号："))
# 发送数据
send_meassage = input("请输入要发送的数据：")
client.sendto(send_meassage.encode('utf8'), (dest_ip, dest_port))
client.close()


