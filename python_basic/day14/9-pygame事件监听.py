# 作者: 王道 龙哥
# 2022年06月14日14时43分48秒
import pygame

# 游戏的初始化
pygame.init()

# 创建游戏的窗口 480 * 700
screen = pygame.display.set_mode((480, 700))

# 绘制背景图像
bg = pygame.image.load("./images/background.png")
screen.blit(bg, (0, 0))
# pygame.display.update()

# 绘制英雄的飞机
hero = pygame.image.load("./images/me1.png")
screen.blit(hero, (150, 300))

# 可以在所有绘制工作完成之后，统一调用update方法
pygame.display.update()

clock = pygame.time.Clock()
# 1. 定义rect记录飞机的初始位置
hero_rect = pygame.Rect(150, 700, 102, 126)
# 游戏循环 -> 意味着游戏的正式开始！
while True:

    # 可以指定循环体内部的代码执行的频率
    clock.tick(60)
    # 捕获事件
    event_list = pygame.event.get()
    # if len(event_list) > 0:
    #     print(event_list)
    for event in event_list:

        # 判断事件类型是否是退出事件
        if event.type == pygame.QUIT:
            print("游戏退出...")

            # quit 卸载所有的模块
            pygame.quit()

            # exit() 直接终止当前正在执行的程序
            exit()

    # 2. 修改飞机的位置
    hero_rect.y -= 1
    if hero_rect.y==-hero_rect.height:
        hero_rect.y=700
    # 3. 调用blit方法绘制图像
    screen.blit(bg, (0, 0))
    screen.blit(hero, hero_rect)

    # 4. 调用update方法更新显示
    pygame.display.update()

pygame.quit()