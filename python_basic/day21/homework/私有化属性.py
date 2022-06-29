# 作者 ： 赖鑫
# 2022年06月22日17时30分58秒
import test_module


class People:
    def __init__(self, name, age, taste):
        self.name = name
        self._age = age
        self.__taste = taste

    def show_people(self):
        print(self.name)
        print(self._age)
        print(self.__taste)

    def _work(self):
        """
        不建议外部使用，但是依然可以使用
        :return:
        """
        print('my_work')

    def __away(self):
        """
        私有方法，对外不可见
        :return:
        """
        print('__my_away')

    def do_work(self):
        self._work()
        self.__away()


class Student(People):
    def construction(self, name, age, taste):
        self.name = name
        self._age = age
        self.__taste = taste  # 父类中的__属性，子类不能继承，子能也不能访问

    def show_student(self):
        print(self.name)
        print(self._age)
        print(self.__taste)

    @staticmethod
    def test_bug():
        test_module._Bug.show_bug()


people = People('lmx', 18, 'spicy')
people.show_people()
people.do_work()
print('-' * 50)

studnet = Student('lx', 19, 'spicy')
studnet.show_student()
studnet.test_bug()
