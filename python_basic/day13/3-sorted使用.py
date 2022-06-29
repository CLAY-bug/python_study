# 作者: 王道 龙哥
# 2022年06月13日11时43分04秒
list1 = [1, 3, 2, 4, 5, 3, 2]
print(sorted(list1))
print(list1)
# 字典排的是键，key
print(sorted({1: 'D', 2: 'B', 4: 'B', 3: 'E', 5: 'A'}))
# 排序的列表，里边是字符串,key不会改变原有的待排序内容，key是排序规则
print(sorted("This is a test string from Andrew".split()))
print(sorted("This is a test string from Andrew".split(), key=str.lower))

print('排序列表嵌套元组-----------')

student_tuples = [

    ('jone', 'B', 12),
    ('dave', 'B', 10),
    ('jahn', 'A', 15),
]


def youming(student):
    return student[1]


# lambda是匿名函数,匿名函数只能用一次，而且逻辑简单
# s就是形参，等价于youming里的student，s[1]就是返回值，等价于student[1]
print(sorted(student_tuples, key=youming))
print(sorted(student_tuples, key=lambda s: s[1]))
print('排序列表内是自定义对象')
class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age
    def __repr__(self):
        """
        str必须返回的是字符串类型，repr和str功能一样，只是可以返回的类型不是字符串
        :return:
        """
        return repr((self.name, self.grade, self.age))

s=Student('john', 'A', 15)
print(s)

student_objects = [
    Student('john', 'A', 15),
    Student('jane', 'B', 12),
    Student('dave', 'B', 10),
]

print(sorted(student_objects, key=lambda s: s.age))

print('operator的使用')
from operator import itemgetter, attrgetter
print(sorted(student_tuples, key=itemgetter(2)))

print(sorted(student_objects, key=attrgetter('age')))

print('同时还支持多层排序')
print(sorted(student_tuples, key=itemgetter(1,2)))

print(sorted(student_objects, key=attrgetter('grade', 'age')))

#降序
print(sorted(student_tuples, key=itemgetter(2),reverse=True))

#是否是稳定排序
data = [('red', 1), ('blue', 1), ('red', 2), ('blue', 2)]
print(sorted(data,key=lambda s:s[0]))

print('排字典')

mydict = { 'Li'   : ['M',7],
         'Zhang': ['E',2],
         'Wang' : ['P',3],
         'Du'   : ['C',2],
         'Ma'   : ['C',9],
         'Zhe'  : ['H',7] }

# for i in mydict.items():
#     print(i)
print(sorted(mydict.items(), key=lambda v: v[1][1]))

print('列表中嵌入字典排序')
gameresult = [
    { "name":"Bob", "wins":10, "losses":3, "rating":75.00 },
    { "name":"David", "wins":3, "losses":5, "rating":57.00 },
    { "name":"Carol", "wins":4, "losses":5, "rating":57.00 },
    { "name":"Patty", "wins":9, "losses":3, "rating": 71.48 }]

print(sorted(gameresult , key=itemgetter("rating","name")))

