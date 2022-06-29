# 作者: 王道 龙哥
# 2022年06月08日11时05分38秒
# 发生异常后，会直接跳入except，try内部，异常位置下面的代码不会得到执行
try:
    num = int(input("请输入整数："))
    result = 8 / num
    print(result)
except ValueError:
    print("请输入正确的整数")
# except ZeroDivisionError:
#     print("除 0 错误")
except Exception as result:
    print("未知错误 %s" % result)  # result记录的是未知异常的信息
