# Creat by PekingMan on 2020/1/16
# 该程序是对窗口的控制程序
# 该程序包括：
# 工具：transparent_blit，是透明度放置工具
# 显示：Hunter_start，在窗口上显示logo

import pygame
from HunterController import HunterController

# 初始化pygame
pygame.init()

# 插入类
HunterController = HunterController()


class HunterWindow:
    pass


class HunterScreen(HunterWindow):
    # 设置窗口标题和窗口大小
    screenCaption = pygame.display.set_caption("Hunter")
    screen = pygame.display.set_mode((800, 500), 0, 32)

    def Hunter_start(self):
        print("logo显示界面")
        # 填充背景为黑色
        pygame.Surface.fill(self.screen, (0, 0, 0))  # 将背景颜色设置为黑色
        pygame.display.update()
        # 加载Start_LogoBlack
        startLogo = (r"D:\Project\Hunter\Image\Start\Start_LogoBlack.png")  # 设置图片路径 图片Start_LogoBlack：宽353，高170
        startLogo = pygame.image.load(startLogo)  # 加载图片
        # 加载Title
        startTitle = (r"D:\Project\Hunter\Image\Start\Title.png")
        startTitle = pygame.image.load(startTitle)
        # 淡入显示图片，透明度从0到255
        print("淡入开始")
        for i in range(0, 256, 15):
            print("startLogo Transparent =", i)  # 输出startLogo的透明度
            print("startTitle Transparent =", i)  # 输出startTitle的透明度
            HunterTools.transparent_blit(self, self.screen, startLogo, (240, 130), i)  # 将startLogo放置在(240, 130)，透明度为i
            HunterTools.transparent_blit(self, self.screen, startTitle, (170, 300), i)  # 将startTitle放置在(170, 300)，透明度为i
            pygame.time.delay(50)  # 等待50毫秒，即0.05秒
            pygame.display.update()
        print("淡入结束")
        # 绘制一个黑色矩形，覆盖startLogo和startTitle
        # 矩形坐标：(170, 100)， 矩形大小：500*300
        pygame.draw.rect(self.screen, (0, 0, 0), (170, 100, 500, 300), 0)
        pygame.display.update()
        # 淡出隐藏图片，透明度从255到0
        print("淡出开始")
        for i in range(0, 256, 15):
            transparentValue = 255 - i
            print("startLogo Transparent =", transparentValue)  # 输出startLogo的透明度
            print("startTitle Transparent =", transparentValue)  # 输出startTitle的透明度
            HunterTools.transparent_blit(self, self.screen, startLogo, (240, 130),
                                  transparentValue)  # 将startLogo放置在(240, 130)，透明度为transparentValue
            HunterTools.transparent_blit(self, self.screen, startTitle, (170, 300),
                                  transparentValue)  # 将startTitle放置在(170, 300)，透明度为transparnetValue
            # 绘制一个黑色矩形，覆盖startLogo和startTitle
            # 矩形坐标：(170, 100)， 矩形大小：500*300
            pygame.draw.rect(self.screen, (0, 0, 0), (170, 100, 500, 300), 0)
            pygame.time.delay(50)  # 等待50毫秒，即0.05秒
            pygame.display.update()
        print("淡出结束")

    def Hunter_menu(self):
        print("主菜单界面")
        # EG：Give Thanks
        if HunterController.EGVerify_giveThanks == True:
            print("EG_giveThanks被触发")


class HunterTools(HunterWindow):
    def transparent_blit(self, surface, image, position, alphaValue):
        # 设置图片坐标
        positionX = position[0]
        positionY = position[1]
        # 创建tempScreen(临时屏幕)后，利用之进行透明度图片放置
        tempScreen = pygame.Surface((pygame.Surface.get_width(image), pygame.Surface.get_height(image)))
        tempScreen.blit(surface, (positionX, positionY))
        tempScreen.blit(image, (0, 0))
        tempScreen.set_alpha(alphaValue)
        surface.blit(tempScreen, (positionX, positionY))
        pygame.display.update()
