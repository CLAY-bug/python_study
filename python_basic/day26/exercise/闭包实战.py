# 作者 ： 赖鑫
# 2022年06月29日08时57分43秒

def make_blod(func):
    def wrapped():
        return "<b>" + func() + "</b>"

    return wrapped


def make_italic(func):
    def wrapped():
        return '<i>' + func() + "</i>"

    return wrapped


@make_blod
def test1():
    return "hello world"


@make_italic
def test2():
    return "hello world2"


@make_blod
@make_italic
def test3():
    return "hello world3"


print(test1())
print(test2())
print('-' * 30)
print(test3())
