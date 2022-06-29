# 作者 ： 赖鑫
# 2022年06月12日20时46分09秒

# 单例射击模式：让类创建的对象在系统中只有唯一的实例

class MusicPlayer:
    # 记录第一个被创建的对象的引用
    instance = None
    # 记录是否执行过初始化动作
    init_flay = False

    def __new__(cls, *args, **kwargs):
        # 判断类属性是否已经被赋值了
        if cls.instance is None:
            # 调用第一个方法，为第一个对象赋值
            cls.instance = super().__new__(cls)
            # 返回类属性保存的对象引用
            return cls.instance
        else:
            return cls.instance

    def __init__(self, music_name):
        if not MusicPlayer.init_flay:
            self.music_name = music_name
            print("初始化音乐播放器")
            MusicPlayer.init_flay = True

    def play_music(self):
        print(f"播放音乐'{self.music_name}'...")


# 实例化对象1
player1 = MusicPlayer("爱你")
player1.play_music()
print(player1)
print('-' * 50)
# 实例化对象1
player2 = MusicPlayer("修炼爱情")
player2.play_music()
print(player2)
