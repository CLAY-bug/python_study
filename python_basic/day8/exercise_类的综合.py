# 作者 ： 赖鑫
# 2022年06月12日20时30分16秒

class Game:
    top_score = 0

    def __init__(self, player_name):
        self.player_name = player_name

    @classmethod
    def show_top_score(cls):
        print(f"当前最高分时{Game.top_score}")

    @staticmethod
    def show_help():
        print("显示游戏帮助信息")

    def start_game(self):
        print(f"{self.player_name}开始游戏")

    def add_score(self, score):
        Game.top_score += score


Game.show_help()
# 创建一个玩家
game = Game('lmx')
# 开始游戏
game.start_game()
# 游戏得分
game.add_score(100)
# 显示得分
Game.show_top_score()





