# 作者: 王道 龙哥
# 2022年06月08日11时16分41秒
try:
    num=1/0
except Exception as e:
    print(e)
    print(e.__traceback__.tb_frame.f_globals["__file__"])   # 发生异常所在的文件
    print(e.__traceback__.tb_lineno)                        # 发生异常所在的行数