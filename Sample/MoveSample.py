import pygame

pygame.init()
screen = pygame.display.set_mode((640, 70))
pygame.display.set_caption("键盘事件")

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((255, 255, 255))

ball = pygame.Surface((30, 30))  # 建立球的矩形背景区
ball.fill((255, 255, 255))  # 矩形区域背景为白色
pygame.draw.circle(ball, (0, 0, 255), (15, 15), 15, 0)  # 画蓝色球

rect1 = ball.get_rect()  # 取得球的矩形背景区域
rect1.center = (320, 35)  # 球的初始位置
x, y = rect1.topleft  # 球左上角坐标
dx = 5  # 球移动距离

clock = pygame.time.Clock()

running = True
while running:
    clock.tick(30)  # 每秒执行30次
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()  # 检查按键是按下
    if keys[pygame.K_RIGHT] and rect1.right < screen.get_width():  # 按向右键且未达右边界
        rect1.centerx += dx  # 向右移动
    elif keys[pygame.K_LEFT] and rect1.left > 0:  # 按向左键且未达左边界
        rect1.centerx -= dx  # 向左移动

    screen.blit(background, (0, 0))  # 清除绘图窗口
    screen.blit(ball, rect1.topleft)
    pygame.display.update()
pygame.quit()