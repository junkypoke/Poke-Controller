#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Commands.PythonCommandBase import PythonCommand, ImageProcPythonCommand
from Commands.Keys import KeyPress, Button, Direction, Stick

class AutoFishing(ImageProcPythonCommand):
    NAME = 'JPN(漢字)釣り色厳選 ver.2.1'

    def __init__(self,cam):
        super().__init__(cam)

    def do(self):
        print("-------------------------------")
        print("JPN(漢字)釣り色厳選 ver.2.1")
        print("Developed by.じゃんきー")
        print("Special Thanks:Mari Ai Ai")
        print("-------------------------------")
        self.wait(0.5)
        count = 1
        print("Start")

        while True:
            self.wait(0.5)
            print("wait...")
            if self.isContainTemplate('Network_Offline.png',0.7, show_value=False):
                print("Offline_Check:OK")
                print("wait...5.5sec")
                self.wait(5.5)
                self.press(Button.A, 0.05)
                while not (self.isContainTemplate('hit.png', threshold=0.9, use_gray=True, show_value=False)):
                    self.wait(0.1)
                self.press(Button.A, 0.05) #つり完了
                while not (self.isContainTemplate('yasei.png', threshold=0.9, use_gray=True, show_value=False) \
                or self.isContainTemplate('late.png', threshold=0.9, use_gray=True, show_value=False)):
                    self.wait(0.1)
                print("判定中...")
                self.wait(2.6) #yaseiからの時間調整
                if self.isContainTemplate('Encount_Ball4.png',0.8, show_value=False):
                    print("通常色")
                    while not (self.isContainTemplate('command.png', threshold=0.9, use_gray=True, show_value=False)):
                        self.wait(0.5)
                        print("wait...")
                    self.wait(0.4)
                    self.press(Direction.UP, 0.1)
                    self.wait(0.4)
                    self.press(Button.A,0.1,4.5)
                    print("試行回数",count,"回") #カウント
                    count += 1
                #釣れなかったときの処理
                elif self.isContainTemplate('late.png',0.8, show_value=False):
                    print("釣り失敗")
                    self.press(Button.A,0.1,4.5)
                else:
                    print("色違い!!")
                    #self.press(Button.CAPTURE,3) #キャプチャー
                    self.finish()
