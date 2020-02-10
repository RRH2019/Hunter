# Creat by PekingMan on 2020/1/16
# 程序的运行逻辑

import pygame
import sys
from HunterWindow import HunterScreen

pygame.init()

class HunterController:
    # 实现点击退出按钮时退出程序
    def exit(self, event):
        if event.type == pygame.QUIT:
            sys.exit()

    # 彩蛋：向全国一线防疫人员致敬
    def EG_giveThanks(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_BACKSPACE] == True:
            HunterScreen.EG_giveThanks(HunterScreen)

    # 大循环
    def while_loop(self):
        while True:
            for event in pygame.event.get():
                # 当点击关闭按钮时退出游戏
                self.exit(event)
                self.EG_giveThanks()