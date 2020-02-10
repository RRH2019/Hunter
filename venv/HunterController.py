# Creat by PekingMan on 2020/1/16
# 程序的运行逻辑

import pygame
import sys
from HunterWindow import HunterScreen

pygame.init()

class HunterController:
    EG_giveThanks_Verify = False

    # 实现点击退出按钮时退出程序
    def exit(self, event):
        if event.type == pygame.QUIT:
            sys.exit()

    # 彩蛋：向全国一线防疫人员致敬
    def EG_giveThanks(self):
        key = pygame.key.get_pressed()
        # 如果EG_giveThanks_Verify == False且按下BACKSPACE
        if not self.EG_giveThanks_Verify and key[pygame.K_BACKSPACE]:
            HunterScreen.EG_giveThanks(HunterScreen)
            self.EG_giveThanks_Verify = True
        # 如果EG_giveThanks_Verify == True且按下BACKSPACE
        elif self.EG_giveThanks_Verify and key[pygame.K_BACKSPACE]:
            HunterScreen.BlackRect(HunterScreen, (0, 0, 0))
            print("EG_giveThanks已关闭")

    # 大循环
    def while_loop(self):
        while True:
            for event in pygame.event.get():
                # 当点击关闭按钮时退出游戏
                self.exit(event)
                # EG_giveThanks检测及触发
                self.EG_giveThanks()