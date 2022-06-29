# 作者: 王道 龙哥
# 2022年06月08日11时41分33秒

#相对于raise，省了一个if

try:
    assert 1==0,"你的程序在这里发生了什么什么错误"
except Exception as e:
    print(e)