# 作者: 王道 龙哥
# 2022年06月06日11时49分55秒
xiaoming = {"name": "小明",
            "age": 18,
            "gender": True,
            "height": 1.75}

print(xiaoming.items())
for i in xiaoming.items(): #字典里遍历最常用的一种操作
    print(i)

#get的使用,get去获取某个键不存在，程序不会崩
ret=xiaoming.get('age1')
print(ret)

#使用fromkeys,初始化一个确定key的字典
student_info=dict.fromkeys(['name','age','sex'],0)
print(student_info)