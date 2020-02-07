# Creat by PekingMan on 2020/1/16

import pygame
import sys

pygame.init()

class HunterController:
    EGVerify_giveThanks = False

    def exit(self, event):
        if event.type == pygame.QUIT:
            sys.exit()

    def EG_giveThanks(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_BACKSPACE] == True:
            self.EGVerify_giveThanks = True
            print("EGVerify_giveThanks = True")

    def while_loop(self):
        while True:
            for event in pygame.event.get():
                self.exit(event)  # 当点击关闭按钮时退出游戏
                self.EG_giveThanks()