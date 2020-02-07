import pygame
import sys
from pygame.locals import *
pygame.init()
size = width,height = 1200,480
bg = (0,0,0)
clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("初次见面，请大家多多关照")

dog = pygame.image.load("D:\Project\Hunter\Image\Start_LogoBlack.png").convert_alpha()
background = pygame.image.load("D:\MyFile\Wall Paper\moon_full_moon_night_city_153478_1366x768.jpg").convert()

position = dog.get_rect()
position.center = width //2,height //2

def blit_alpha(target,source,location,opacity):
    x = location[0]
    y = location[1]
    temp = pygame.Surface((source.get_width(),source.get_height())).convert()
    temp.blit(target,(-x,-y))
    temp.blit(source,(0,0))
    temp.set_alpha(opacity)
    target.blit(temp,location)

# 设置为死循环，确保窗口一直显示
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # 更新图像
    screen.blit(background,(0,0))
    blit_alpha(screen,dog,position,50)
    # 更新界面
    pygame.display.flip()

    clock.tick(30)