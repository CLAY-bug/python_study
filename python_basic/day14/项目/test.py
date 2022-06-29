import pygame
import time

pygame.init()
pygame.mixer.init()

pingmu = pygame.display.set_mode([500, 365])
m = "./sound/use_bomb.wav"
pygame.mixer.music.load(m)
pygame.mixer.music.play()
time.sleep(5)
