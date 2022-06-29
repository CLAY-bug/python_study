# 作者 ： 赖鑫
# 2022年06月13日16时47分17秒

def input_pwd():
    pwd = input("请输入密码：")
    if len(pwd) >= 8:
        return pwd
    else:
        raise Exception("密码长度不够")

try:
    print(input_pwd())
except Exception as e:
    print(e)
