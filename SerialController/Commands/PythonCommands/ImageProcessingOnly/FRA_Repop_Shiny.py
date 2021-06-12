#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Commands.PythonCommandBase import PythonCommand, ImageProcPythonCommand
from Commands.Keys import KeyPress, Button, Direction, Stick, Hat

class AutoEncount(ImageProcPythonCommand):
    NAME = 'FRA_リポップ色違い厳選'

    def __init__(self,cam):
        super().__init__(cam)

    def do(self):
        print("-------------------------------")
        print("FRAリポップ色違い厳選 ver.1.0")
        print("Developed by.じゃんきー")
        print("-------------------------------")
        self.wait(0.5)
        count = 1
        print("Start")

        while True:
            self.wait(0.5)
            while not self.isContainTemplate('yasei_FRA.png', threshold=0.8, use_gray=True, show_value=False):
                self.press(Button.A, wait=0.3)
            print("判定中...")
            self.wait(2.6) #yaseino！からの時間調整
            if self.isContainTemplate('Encount_Ball4.png',0.8, use_gray=False, show_value=False):
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