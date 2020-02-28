# Creat by PekingMan on 2020/1/16
# 程序的运行逻辑

import pygame
import sys
from HunterWindow import HunterScreen
from HunterWindow import HunterTools

pygame.init()

class HunterController:
    EG_giveThanks_Verify = False

    # 实现点击退出按钮时退出程序
    def exit(self, event):
        if event.type == pygame.QUIT:
            sys.exit()

    def Hunter_menu_biggerText(self, event):
        # 获取鼠标位置
        mousePos = pygame.mouse.get_pos()
        mousePos_x = mousePos[0]
        mousePos_y = mousePos[1]
        # 当鼠标移动到start上方时
        if 320 <= mousePos_x <= 495 and 400 <= mousePos_y <= 470:
            HunterScreen.Hunter_menu_biggerText_bigger(HunterScreen)
            if event.type == pygame.MOUSEBUTTONDOWN:
                print("按下start")
        # 当鼠标离开start时
        else:
            HunterScreen.Hunter_menu_biggerText_smaller(HunterScreen)

    # 彩蛋：向全国一线防疫人员致敬
    def EG_giveThanks(self):
        key = pygame.key.get_pressed()
        # 如果EG_giveThanks_Verify == False且按下BACKSPACE
        if not self.EG_giveThanks_Verify and key[pygame.K_BACKSPACE]:
            # 刷新屏幕，放置menu出现在屏幕上
            HunterTools.BlackRect(HunterTools, (0, 0, 0))
            # 执行HunterScreen中的EG_giveThanks函数
            HunterScreen.EG_giveThanks(HunterScreen)
            # 令EG_giveThanks_Verify为True使得该彩蛋无法再次触发
            self.EG_giveThanks_Verify = True
        # 如果EG_giveThanks_Verify == True且按下BACKSPACE
        elif self.EG_giveThanks_Verify and key[pygame.K_BACKSPACE]:
            # 刷新屏幕
            HunterTools.BlackRect(HunterTools, (0, 0, 0))
            print("EG_giveThanks已关闭")
            # 显示menu界面
            HunterScreen.Hunter_menu(HunterScreen)