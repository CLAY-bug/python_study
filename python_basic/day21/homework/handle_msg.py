# 作者 ： 赖鑫
# 2022年06月22日19时37分06秒

import common
from common import RECV_DATA_LIST


def handle_data():
    """模拟处理recv_msg模块接收的数据"""
    print("---->handle_data")
    for i in RECV_DATA_LIST:
        print(i)
        common.HANDLE_FLAG = True


def test_handle_data():
    """测试处理是否完成，变量是否设置为True"""
    print("--->test_handel_data")
    if common.HANDLE_FLAG:
        print('----已经处理完成----')
    else:
        print("----未处理完成----")
