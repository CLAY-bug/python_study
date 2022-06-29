# 作者 ： 赖鑫
# 2022年06月23日19时00分51秒
class World:
    county = "China"

    def __init__(self):
        self.original_population = 1.3

    def provice(self, city):
        """实例方法"""
        print(f"{city}是中国的")

    @property
    def population(self):
        """可以把此方法当作属性用"""
        brefor_population = self.original_population * 10
        return brefor_population

    @population.setter
    def population(self, number):
        """设置property属性的值"""
        self.original_population = number

    @population.deleter
    def population(self):
        """通过此方法可以删除属性并打出日志"""
        print("马上删除population这个属性了")


china = World()
print(f'中国有{china.population}亿的人口')  # 通过property装饰器把类中的方法当作属性来使用
china.population = 1.4  # 修改property属性的值
print(f'中国有{china.population}亿的人口')
del china.population
