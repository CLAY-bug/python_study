# 作者: 王道 龙哥
# 2022年06月07日14时41分52秒
class HouseItem:
    """
    家具类
    """

    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return "[%s] 占地 %.2f" % (self.name, self.area)


# 1. 创建家具
bed = HouseItem("席梦思", 4)
chest = HouseItem("衣柜", 2)
table = HouseItem("餐桌", 1.5)

print(bed)
print(chest)
print(table)
print('-' * 50)


class House:

    def __init__(self, house_type, area):
        self.house_type = house_type
        self.area = area

        # 剩余面积
        self.free_area = area

        # 家具名称列表
        self.item_list = []

    def __str__(self):
        # Python 能够自动的将一对括号内部的代码连接在一起
        return ("户型：%s\n总面积：%.2f[剩余：%.2f]\n家具：%s"
                % (self.house_type, self.area,
                   self.free_area, self.item_list))
    #在一个形参后，通过冒号加注解，能够联想，提高编程效率
    def add_item(self, item:HouseItem):
        print("要添加 %s" % item)
        if self.free_area<item.area:
            print('房间面积不够')
            return
        self.item_list.append(item.name)
        self.free_area-=item.area


# 2. 创建房子对象
my_home = House("两室一厅", 60)

my_home.add_item(bed)
my_home.add_item(chest)
my_home.add_item(table)
print(my_home)