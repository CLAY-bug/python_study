# 作者: 王道 龙哥
# 2022年06月06日11时33分54秒
xiaoming = {"name": "小明",
            "age": 18,
            "gender": True,
            "height": 1.75}

print(xiaoming['name'])
print('-'*50)
for k in xiaoming:
    print("%s: %s" % (k, xiaoming[k]))

xiaoming_dict = {"name": "小明"}
# 1. 取值
print(xiaoming_dict["name"])
# 在取值的时候，如果指定的key不存在，程序会报错！
# print(xiaoming_dict["name123"])

# 2. 增加/修改
# 如果key不存在，会新增键值对
xiaoming_dict["age"] = 18
# 如果key存在，会修改已经存在的键值对
xiaoming_dict["name"] = "小小明"
xiaoming_dict.setdefault('name','小月亮')  #对应键不存在的时候插入，存在时不改动

print(xiaoming_dict)
print('-'*50)
# 3. 删除
xiaoming_dict.pop("name")
# 在删除指定键值对的时候，如果指定的key不存在，程序会报错！
# xiaoming_dict.pop("name123")

print(xiaoming_dict)
print('-'*50)

xiaoming_dict = {"name": "小明",
                 "age": 18}

# 4. 统计键值对数量
print(len(xiaoming_dict))

# 5. 合并字典
temp_dict = {"height": 1.75,
             "age": 20}

# 注意：如果被合并的字典中包含已经存在的键值对，会覆盖原有的键值对
print(id(xiaoming_dict))
xiaoming_dict.update(temp_dict)
print(xiaoming_dict)
print(id(xiaoming_dict))
print('-'*50)
# 6. 清空字典
xiaoming_dict.clear()

print(xiaoming_dict)