# 作者 ： 赖鑫
# 2022年06月22日19时43分03秒

import recv_msg
import handle_msg


def main():
    # 接收数据
    recv_msg.recv_msg()
    # 测试是否接收完毕
    recv_msg.test_recv_data()
    # 判断如果处理完成，则接收其他数据
    recv_msg.recv_msg_next()
    # 测试是否处理完毕
    handle_msg.test_handle_data()
    # 判断如果处理完成，则接收其他数据
    recv_msg.recv_msg_next()


if __name__ == '__main__':
    main()
