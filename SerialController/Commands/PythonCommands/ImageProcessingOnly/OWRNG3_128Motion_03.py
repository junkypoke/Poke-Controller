#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Commands.PythonCommandBase import PythonCommand, ImageProcPythonCommand
from Commands.Keys import KeyPress, Button, Direction, Stick
from Commands.PythonCommands.ImageProcessingOnly import OWRNG0_Setting_03

class lipoopu(ImageProcPythonCommand):
    NAME = 'OWRNG3_128Motion_03'

    def __init__(self,cam):
        super().__init__(cam)

    def do(self):
        print("-------------------------------")
        print("OWRNG3_128Motion_03")
        print("Development:Junky/アキルノ")
        print('')
        print(OWRNG0_Setting_03.motion_full,'回 測定します')
        print("-------------------------------")

        # 0が物理技で1が特殊技

        count = 0
        s = 'Morion:'
        print('')

        while count <  OWRNG0_Setting_03.motion_full: #消費回数を入力する
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
            print(s)
            print("-------------------------------")
        
        s128 = s
        print("------------RESULT-------------")
        print("消費数",count,"F")
        print('すべてのモーション')
        print(s)
        print('下128桁')
        print(s128[-128:])
        print("------------FINISH-------------")
        self.finish()

