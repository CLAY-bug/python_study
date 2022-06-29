# 作者 ： 赖鑫
# 2022年06月28日20时35分38秒

def test(number):
    def test_in(number_in):
        print(f'number_in is {number_in}')
        return number + number_in

    return test_in


ret = test(20)  # 即ret = test_in()
print(ret(100))
