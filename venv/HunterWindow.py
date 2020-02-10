# Creat by PekingMan on 2020/1/16
# 该程序是对窗口的控制程序，程序的运行逻辑可在HunterController.py中查看
# 该程序包括：工具（HunterTools）和显示（HunterScreen）
# 工具：transparent_blit，是透明度放置工具
# 显示：Hunter_start，在窗口上显示logo

import pygame

# 初始化pygame
pygame.init()


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
        pass

    # 彩蛋：致敬全国抗疫一线工作者
    def EG_giveThanks(self):
        print("EG_giveThanks已被触发")
        # 颜色
        white = (255, 255, 255)
        # 输出文字
        HunterTools.textPrint(HunterTools, r"C:\Windows\Fonts\simhei.ttf", 30, "今天是2020年2月11日，新型冠状病毒在中国", white, (0, 0))
        HunterTools.textPrint(HunterTools, r"C:\Windows\Fonts\simhei.ttf", 30, "已经爆发三个月了，现有确诊人数40261例，治愈", white, (0, 30))
        HunterTools.textPrint(HunterTools, r"C:\Windows\Fonts\simhei.ttf", 30, "3494例，死亡909例。包括我在内的绝大多数北京", white, (0, 60))
        HunterTools.textPrint(HunterTools, r"C:\Windows\Fonts\simhei.ttf", 30, "人都在家中等待疫情过去，但那些一线的医生、护", white, (0, 90))
        HunterTools.textPrint(HunterTools, r"C:\Windows\Fonts\simhei.ttf", 30, "士、科学家却仍在最危险的地区治疗病人，照顾病", white, (0, 120))
        HunterTools.textPrint(HunterTools, r"C:\Windows\Fonts\simhei.ttf", 30, "人，为世界对病毒的抗争做出卓越的贡献。在此，", white, (0, 150))
        HunterTools.textPrint(HunterTools, r"C:\Windows\Fonts\simhei.ttf", 30, "我向这些英雄，致以崇高的敬意。————PekingMan", white, (0, 180))

    # 绘制一个覆盖全屏的颜色方块，相当于刷新屏幕
    def BlackRect(self, color):
        pygame.draw.rect(self.screen, color, (0, 0, 800, 500), 0)
        pygame.display.update()


class HunterTools(HunterWindow):
    # 该函数用于放置可调节透明度图片
    def transparent_blit(self, surface, image, position, alphaValue):
        # 图片坐标
        positionX = position[0]
        positionY = position[1]
        # 创建tempScreen(临时屏幕)后，利用之进行透明度图片放置
        tempScreen = pygame.Surface((pygame.Surface.get_width(image), pygame.Surface.get_height(image)))
        tempScreen.blit(surface, (positionX, positionY))
        tempScreen.blit(image, (0, 0))
        tempScreen.set_alpha(alphaValue)
        surface.blit(tempScreen, (positionX, positionY))
        pygame.display.update()

    # 在屏幕上打印文本
    def textPrint(self, font, size, text, color, position):
        # 确定文字字体与大小
        myFont = pygame.font.Font(font, size)
        # 确定文本内容和颜色
        myText = myFont.render(text, True, color)
        # 根据位置输出文本（position[0]为x坐标，position[1]为y坐标）
        HunterScreen.screen.blit(myText, (position[0], position[1]))
        pygame.display.update()
