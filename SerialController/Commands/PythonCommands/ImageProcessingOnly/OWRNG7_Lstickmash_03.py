#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Commands.PythonCommandBase import PythonCommand, ImageProcPythonCommand
from Commands.Keys import KeyPress, Button, Direction, Stick
import time
from Commands.PythonCommands.ImageProcessingOnly import OWRNG0_Setting_03

class OWRNG7(ImageProcPythonCommand):
    NAME = 'OWRNG7_Lstick_mash_03'

    def __init__(self,cam):
        super().__init__(cam)


    def do(self):
        framecount = OWRNG0_Setting_03.frame_Lstick #消費したいフレーム数

        print("OWRNG7_Lstick_mash_03")
        print("Development:Junky")
        print("-------------------------------")
        print(" ")
        print(framecount,"F消費します")
        print("予測時間は",OWRNG0_Setting_03.time_estimate,"秒です")
        print(" ")
        print("-------------------------------")

        count = 0
        time_sta = time.time()
        s = 'COUNT:'
        print('')

        while count < int(framecount): #消費回数
            self.press(Button.LCLICK,0.05,0.05)
            count += 1

            if int(count) % 50 == 0:
                print("-------------------------------")
                print("消費",count,"F")
                print("-------------------------------")
            
        
        time_end = time.time()
        TIME = time_end - time_sta
        s128 = s
        print("------------RESULT-------------")
        print("経過時間")
        print(TIME,"sec")
        print("消費数",count,"F")
        print("------------FINISH-------------")
        self.finish()

