# Creat by PekingMan on 2020/1/16
# 主程序

import HunterWindow
import HunterController
import pygame

pygame.init()

if "__main__" == __name__:
    HunterWindow.HunterScreen.Hunter_start(HunterWindow.HunterScreen)
    HunterWindow.HunterScreen.Hunter_menu(HunterWindow.HunterScreen)

    while True:
        for event in pygame.event.get():
            # 点击关闭按钮退出游戏
            HunterController.HunterController.exit(HunterController.HunterController, event)
            # EG_giveThanks
            HunterController.HunterController.EG_giveThanks(HunterController.HunterController)
            # menu页面鼠标移到start按钮时start字样放大
            HunterController.HunterController.Hunter_menu_biggerText(HunterController.HunterController, event)