# 作者: 王道 龙哥
# 2022年06月14日11时38分54秒
import pygame
pygame.init()
hero_rect = pygame.Rect(100, 500, 120, 125)

print("英雄的原点 %d %d" % (hero_rect.x, hero_rect.y))
print("英雄的尺寸 %d %d" % (hero_rect.width, hero_rect.height))
# size 属性会返回矩形区域的 (宽, 高) 元组
print("%d %d" % hero_rect.size)