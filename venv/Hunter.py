# Creat by PekingMan on 2020/1/16
# 主程序

import HunterWindow
import HunterController

if "__main__" == __name__:
    # 插入类
    HunterWindow = HunterWindow.HunterScreen()
    HunterController = HunterController.HunterController()
    # 正式运行
    # screen设置和开始界面显示
    HunterWindow.Hunter_start()
    HunterWindow.Hunter_menu()
    # 程序逻辑控制，具体显示内容可在函数while_loop中查看
    HunterController.while_loop()