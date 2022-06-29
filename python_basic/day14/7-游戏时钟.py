# 作者: 王道 龙哥
# 2022年06月14日14时39分56秒
# 3. 创建游戏时钟对象
import pygame
clock = pygame.time.Clock()
i = 0

# 游戏循环
while True:

    # 设置屏幕刷新帧率，每秒60次
    clock.tick(60)

    print(i)
    i += 1