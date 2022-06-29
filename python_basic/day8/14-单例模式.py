# 作者: 王道 龙哥
# 2022年06月07日16时51分36秒
class MusicPlayer:
    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
            return cls.instance
        return cls.instance

    def __init__(self, music_name):
        print('初始化:' + music_name)


player1 = MusicPlayer('青花瓷')
del player1
player2 = MusicPlayer('本草纲目')
# print(player1)
print(player2)
# print(player1 is player2)
