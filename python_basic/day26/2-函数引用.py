# 作者: 王道 龙哥
# 2022年06月28日16时20分51秒
def test1():
    print("--- in test1 func----")

test1()

ret=test1

print(id(test1))
print(id(ret))