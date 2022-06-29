# 作者: 王道 龙哥
# 2022年06月08日11时32分40秒
def input_password():

    # 1. 提示用户输入密码
    pwd = input("请输入密码：")

    # 2. 判断密码长度 >= 8，返回用户输入的密码
    if len(pwd) >= 8:
        return pwd

    # 3. 如果 < 8 主动抛出异常
    print("主动抛出异常")
    # 1> 创建异常对象 - 可以使用错误信息字符串作为参数
    # 2> 主动抛出异常
    raise Exception("密码长度不够")
    print('你看不到我')

# 提示用户输入密码
try:
    print(input_password())
except Exception as result:
    print(result)  #result中得到的就是raise回来的东西， "密码长度不够"