# 作者 ： 赖鑫
# 2022年06月12日10时28分54秒

class Gun:
    """枪类"""
    def __init__(self, model):
        # 枪的型号
        self.model = model
        # 子弹数量
        self.bullet_count = 0

    def add_bullet(self, count):
        # 添加子弹
        self.bullet_count += count

    def shoot(self):
        # 判断是否有子弹
        if self.bullet_count <= 0:
            print("子弹数不足，不能射击...")
        else:
            self.bullet_count -= 1
            print("开枪射击，剩余子弹数为：%d" % self.bullet_count)


class Soldier:
    """士兵类"""
    # 初始士兵都没有枪
    def __init__(self, name):
        self.name = name
        self.gun:Gun = None

    def add_gun(self, gun):
        self.gun = gun
        print("%s捡了一把%s枪" %(self.name, self.gun.model))

    def fire(self):
        if self.gun is None:
            print("%s还没有枪" % self.name)
            return
        # 喊口号
        print("冲啊...%s" % self.name)

        # 让枪装子弹
        self.gun.add_bullet(50)
        self.gun.shoot()


ak47 = Gun("AK47")
xusanduo = Soldier("许三多")
xusanduo.add_gun(ak47)
xusanduo.fire()



