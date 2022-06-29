# 作者: 王道 龙哥
# 2022年06月07日09时59分27秒
# 必须把keyword参数放在后面

def demo1(*args, **kwargs):
    print(args)
    print(kwargs)


def demo(*args, **kwargs):
    # print(num)
    demo1(*args[1:], **kwargs)


if __name__ == '__main__':
    tuple1 = (1, 2, 3, 4, 5)
    dict1 = {'name': '小明', 'age': 18, 'gender': True}
    # 元组拆包，把一个元组变为 调用函数时，实参传递的样子
    # 字典拆包，把一个字典变为 调用函数时，kw实参传递的样子
    demo(*tuple1, **dict1)
