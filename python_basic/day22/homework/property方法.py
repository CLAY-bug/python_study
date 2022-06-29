# 作者 ： 赖鑫
# 2022年06月23日19时28分00秒
class Exercise:
    def test(self):
        return "lx"

    def set_test(self, new_name):
        print(f'my new name is {new_name}')

    def del_test(self):
        print('i will be delete')

    Test = property(test, set_test, del_test, "这是property方法哦")


exercise = Exercise()
print(exercise.Test)
exercise.Test = 'xxx'
del exercise.Test
