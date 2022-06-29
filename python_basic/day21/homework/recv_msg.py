# 作者 ： 赖鑫
# 2022年06月22日18时53分33秒

import common
from common import RECV_DATA_LIST


def recv_msg():
    """模拟接收数据，然后添加到common模块中的列表中"""
    print("--->recv_msg")
    for i in range(5):
        RECV_DATA_LIST.append(i)


def test_recv_data():
    """测试接收到的数据"""
    print("--->test_recv_data")
    print(RECV_DATA_LIST)


def recv_msg_next():
    """已经处理完成后，再接收到另外的其他数据"""
    print("--->recv_msg_next")
    if common.HANDLE_FLAG:
        print("----发现之前的数据都已经完成，这里进行接收到其他的数据")
    else:
        print("----发现之前的数据未处理完，等待中。。。----")
