#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Commands.PythonCommandBase import PythonCommand, ImageProcPythonCommand
from Commands.Keys import KeyPress, Button, Direction, Stick
import time
from Commands.PythonCommands.ImageProcessingOnly import OWRNG0_Setting_03

class OWRNG(ImageProcPythonCommand):
    NAME = 'OWRNG6_Waiting_03'

    def __init__(self,cam):
        super().__init__(cam)

    def do(self):
        count_t = 0
        wait_count = OWRNG0_Setting_03.waiting_sec # OWRNG0_Setting_03.py

        print("OWRNG6_Waiting_03")
        print("Development:Junky")
        print("-------------------------------")
        print(wait_count,"秒　待機します")
        print("-------------------------------")
        

        while not self.isContainTemplate('OWRNG/YY.png',threshold=0.8, use_gray=True, show_value=False):
            self.press(Button.B,0.1,0.1)
        
        print("待機開始")

        #待機時間
        while count_t < int(wait_count): 
            self.wait(1)
            count_t += 1

            if int(count_t) % 5 == 0:
                print("-------------------------------")
                print("待機時間：",count_t,"秒")
                print("-------------------------------")

        self.press(Button.X,0.1,2.0)
        self.press(Button.A,0.1,1.0)

        print("------------RESULT-------------")
        print("待機時間")
        print(count_t,"秒")
        print("------------FINISH-------------")
        self.finish()


