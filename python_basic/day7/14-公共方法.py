# 作者: 王道 龙哥
# 2022年06月06日16时21分29秒
num_str = "0123456789"
num_list = list(num_str)
print(num_list)
print(num_list[0:7:2])

# 列表中有字典
students = [
    {"name": "阿土",
     "age": 20,
     "gender": True,
     "height": 1.7,
     "weight": 75.0},
    {"name": "小美",
     "age": 19,
     "gender": False,
     "height": 1.6,
     "weight": 45.0},
]
for s in students:
    print(s)

print('-' * 50)
poem = ["\t\n登鹳雀楼",
        "王之涣",
        "白日依山尽\t\n",
        "黄河入海流",
        "欲穷千里目",
        "更上一层楼"]

for poem_str in poem:
    # 先使用strip方法去除字符串中的空白字符
    # 再使用center方法居中显示文本
    print("|%s|" % poem_str.strip().center(10, "　"))

print('-' * 50)
# zip的使用
a = (1, 2, 3)
b = ('a', 'b', 'c')

print(list(zip(a, b)))
# 如何使用enumerate
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
list2 = list(enumerate(seasons))
dict1 = {}
for i in list2:
    dict1[i[1]] = i[0]
print(dict1)
