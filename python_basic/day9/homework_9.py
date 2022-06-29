# 作者 ： 赖鑫
# 2022年06月13日18时14分20秒

def symmetric_num(num):
    """判断是否是对称数"""
    temp = str(num)

    for i in range(len(temp) // 2):
        if temp[i] == temp[-(i + 1)]:
            continue
        else:
            raise Exception("这不是对称数")
    print("这是对称数")


def symmetric_int_num():
    """判断是都是对称整型数"""
    result = input("请输入整形数：")
    if result.isdigit():
        temp = int(result)
        symmetric_num(temp)
    else:
        raise Exception("这不是一个整数！")


try:
    symmetric_int_num()
except Exception as e:
    print(e)
