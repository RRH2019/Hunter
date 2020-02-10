# Creat by PekingMan on 2020/1/16
# 主程序

import HunterWindow
import HunterController

if "__main__" == __name__:
    # 插入类
    HunterWindow = HunterWindow.HunterScreen()
    HunterController = HunterController.HunterController()
    # 正式运行
    HunterWindow.Hunter_start()  # 屏幕设置和开始界面
    HunterWindow.Hunter_menu()
    HunterController.while_loop()  # while循环检测