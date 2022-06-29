# 作者: 王道 龙哥
# 2022年06月07日14时55分08秒
class Gun:

    def __init__(self, model):
        # 枪的型号
        self.model = model
        # 子弹数量
        self.bullet_count = 0

    def add_bullet(self, count):
        self.bullet_count += count

    def shoot(self):
        # 判断是否还有子弹
        if self.bullet_count <= 0:
            print("没有子弹了...")

            return

        # 发射一颗子弹
        self.bullet_count -= 1

        print("%s 发射子弹[%d]..." % (self.model, self.bullet_count))

    def __str__(self):
        return str(self.bullet_count)

# 创建枪对象
ak47 = Gun("ak47")
ak47.add_bullet(50)
ak47.shoot()

class Soldier:

    def __init__(self, name):

        # 1. 姓名
        self.name = name

        # 2. 枪 - 新兵没有枪
        self.gun:Gun = None

    def fire(self):

        # 1. 判断士兵是否有枪
        # if self.gun == None:
        if self.gun is None:
            print("[%s] 还没有枪..." % self.name)

            return

        # 2. 高喊口号
        print("冲啊...[%s]" % self.name)

        # 3. 让枪装填子弹
        self.gun.add_bullet(50)

        # 4. 让枪发射子弹
        self.gun.shoot()

# 1. 创建枪对象
ak47 = Gun("AK47")

# 2. 创建许三多
xusanduo = Soldier("许三多")

xusanduo.gun = ak47
xusanduo.fire()

print(xusanduo.gun)