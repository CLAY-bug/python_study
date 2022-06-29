# 作者: 王道 龙哥
# 2022年06月06日09时47分23秒

import mymodule

if __name__ == '__main__':
    # 因为导入模块时，对应模块的__name__是模块名，而不是main
    print(mymodule.__name__)

    # 当前的__name__是__main__
    print(__name__)
    mymodule.demo1()
