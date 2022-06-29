import socket


def send_msg(udp_socket):
    """获取键盘数据，并将其发送给对方"""
    msg = input("请输入要发送的数据：")
    dest_ip = input("请输入对方的ip地址：")
    dest_port = int(input("请输入对方的端口号"))
    udp_socket.sendto(msg.encode('utf8'), (dest_ip, dest_port))


def recv_msg(udp_socket):
    """显示接受数据"""
    recv_msg = udp_socket.recvfrom(1024)
    recv_ip = recv_msg[1]
    recv_data = recv_msg[0].decode('utf8')
    print(f'>>> ({recv_ip}),({recv_data})')


def main():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind(('', 2000))
    while True:
        op_num = input("请输入数字(1发2收)：")
        if op_num == '1':
            send_msg(udp_socket)
        else:
            recv_msg(udp_socket)


if __name__ == '__main__':
    main()