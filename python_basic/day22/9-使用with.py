# 作者: 王道 龙哥
# 2022年06月23日11时33分12秒

def m2():
    f = open('file', 'r')
    try:
        f.write('人生苦短，我用python')
    except IOError:  # f不能写的时候
        print('oops')
    finally:
        f.close()
        # print(f)


def m3():
    # with没有捕捉异常，只是实现了离开with后，f会close
    with open('file', 'w', encoding='utf8') as f:
        f.write('人生苦短，我用python')


if __name__ == '__main__':
    m2()
    m3()
