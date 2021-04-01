#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Commands.PythonCommandBase import PythonCommand, ImageProcPythonCommand
from Commands.Keys import KeyPress, Button, Direction, Stick, Hat

class AutoEncount(ImageProcPythonCommand):
    NAME = 'JPN(漢字)空中リポップ色違い厳選 ver.1.0'

    def __init__(self,cam):
        super().__init__(cam)

    def do(self):
        print("-------------------------------")
        print("JPN(漢字)空中リポップ色違い厳選 ver.1.0")
        print("Developed by.じゃんきー")
        print("Special Thanks : 優羽")
        print("-------------------------------")
        self.wait(0.5)
        count = 1
        print("Start")

        while True:
            self.wait(0.5)
            self.press(Button.A, 0.2)
            if self.isContainTemplate('Network_Offline.png',0.7, show_value=False):
                print("Offline_Check:OK")
                count2 = 1
                self.press(Button.LCLICK, 0.2)
                while not self.isContainTemplate('yasei.png', threshold=0.8, use_gray=True, show_value=False):
                    self.wait(0.1)
                    count2 += 1
                    if int(count2) % 20 == 0:
                        self.press(Button.LCLICK, 0.2)
                print("判定中...")
                self.wait(2.6) #yaseino！からの時間調整
                if self.isContainTemplate('Encount_Ball4.png',0.7, use_gray=False, show_value=False):
                    self.wait(0.4)
                    print("試行回数",count,"回") #カウント
                    count += 1
                    print("Reset")
                    self.press(Button.HOME, wait=0.5)
                    self.press(Button.X, wait=0.5)
                    self.press(Button.A, wait=2.0)  #closed
                else:
                    print("色違い!!")
                    #self.press(Button.CAPTURE,3) #キャプチャー
                    self.finish()