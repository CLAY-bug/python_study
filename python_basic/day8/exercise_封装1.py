# 作者 ： 赖鑫
# 2022年06月11日19时40分20秒

class HouseItem:
    """ 家具类"""

    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return "我是%s, 占地%f" % (self.name, self.area)


class House:
    """房子类"""

    def __init__(self, house_type, area):
        self.house_type = house_type
        self.area = area
        self.free_area = area  # 初始剩余面积等于房子面积
        self.item = []  # 初始家具列表为空

    def __str__(self):
        return "户型: %s\n总面积: %.2f\n剩余: %.2f\n家具: %s" % (self.house_type, self.area, self.free_area, self.item)

    def add_item(self, item: HouseItem):
        if self.free_area < item.area:
            print('房子空间不足，不能添加家具了')
            return
        else:
            self.free_area -= item.area
            self.item.append(item.name)
            print("%s添加成功!" % item.name)


# 创建家具
bed = HouseItem('床', 5)
chest = HouseItem('衣柜', 4)
table = HouseItem('餐桌', 2)

# 创建房间
my_home = House('三室两厅', 6)

# 添加家具
my_home.add_item(bed)
my_home.add_item(table)
my_home.add_item(chest)
print(my_home)
