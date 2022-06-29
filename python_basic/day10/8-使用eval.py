# 作者: 王道 龙哥
# 2022年06月09日16时26分16秒
import os
def use_eval():
    """
    读取配置文件
    :return:
    """
    f=open('network','r+',encoding='utf8')
    net_info=eval(f.read())
    print(type(net_info))
    print(net_info)

def dont_use_eval():
    """
    未知字符串有安全风险
    :return:
    """
    eval("__import__('os').system('ls')")

if __name__ == '__main__':
    dont_use_eval()