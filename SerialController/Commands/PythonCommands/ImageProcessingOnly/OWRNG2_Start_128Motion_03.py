#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Commands.PythonCommandBase import PythonCommand, ImageProcPythonCommand
from Commands.Keys import KeyPress, Button, Direction, Stick
import time
from Commands.PythonCommands.ImageProcessingOnly import OWRNG0_Setting_03

class lipoopu(ImageProcPythonCommand):
    NAME = 'OWRNG2_Start_128Motion_03'

    def __init__(self,cam):
        super().__init__(cam)

    def do(self):
        print("-------------------------------")
        print("OWRNG2_Start_128Motion_03")
        print("Development:Junky/アキルノ")
        print('')
        print('ソフト起動後',OWRNG0_Setting_03.motion_full,'回 測定します')
        print("-------------------------------")
        
        # ソフト起動時のモーションをカウントします。
        # 0が物理技で1が特殊技

        count = 0
        s = 'Motion:'
        print('')
        time_sta = time.time()

        while not self.isContainTemplate('OWRNG/YY.png',threshold=0.8, use_gray=True, show_value=False):
            self.press(Button.A,0.1,0.1)
        
        self.press(Button.X,0.1,2.0)
        self.press(Button.A,0.1,1.0)
        self.press(Button.A,0.1,1.0)
        self.press(Button.A,0.1,1.0)
        self.press(Button.A,0.1,3.0)

        while count < OWRNG0_Setting_03.motion_full: #消費回数を入力する
            self.press(Button.LCLICK,0.1,1.2)

            #self.wait(0.1) # タイミング調整

            # 閾値調整用
            #self.isContainTemplate('butsuri.png',threshold=0.85, show_value=True)
            # self.isContainTemplate('tokusyu.png',threshold=0.7, show_value=True)

            if self.isContainTemplate('OWRNG/butsuri.png',threshold=0.8,show_value=True):
                print(0 , end='')
                print('物理技モーション')
                s += str(0)
            else:
                print(1 , end='')
                print('特殊技モーション')
                s += str(1)

            self.wait(OWRNG0_Setting_03.wait_Lstick) # タイミング調整
            count += 1

            print("-------------------------------")
            print("測定回数",count,"回")
            print("-------------------------------")
        
        time_end = time.time()
        TIME = time_end - time_sta
        s128 = s
        print("------------RESULT-------------")
        print("経過時間")
        print(TIME,"sec")
        print("消費数",count,"F")
        print('すべてのモーション')
        print(s)
        print('下128桁')
        print(s128[-128:])
        print("------------FINISH-------------")
        self.finish()


