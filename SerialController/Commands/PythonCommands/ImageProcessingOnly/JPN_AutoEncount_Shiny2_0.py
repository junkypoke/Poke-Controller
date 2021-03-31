#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Commands.PythonCommandBase import PythonCommand, ImageProcPythonCommand
from Commands.Keys import KeyPress, Button, Direction, Stick

class AutoEncount(ImageProcPythonCommand):
    NAME = 'JPN(漢字)ランダム・シンボル色厳選 ver.2.0'

    def __init__(self,cam):
        super().__init__(cam)

    def do(self):
        print("-------------------------------")
        print("JPN(漢字)ランダム・シンボル色厳選 ver.2.0")
        print("Developed by.じゃんきー")
        print("Special Thanks:Mari Ai Ai")
        print("-------------------------------")
        self.wait(0.5)
        count = 1
        print("Start")

        while True:
            self.wait(0.5)
            print("wait...")
            if self.isContainTemplate('command.png',0.8, show_value=False):
                self.press(Direction.UP, 0.1)
                self.wait(0.4)
                self.press(Button.A,0.1,4.5)
            #プログラム開始までの処理
            if self.isContainTemplate('Network_Offline.png',0.7, show_value=False):
                print("Offline_Check")
                while not (self.isContainTemplate('yasei.png', threshold=0.9, use_gray=True, show_value=False) \
                    or self.isContainTemplate('yasei2.png', threshold=0.9, use_gray=True, show_value=False)):
                    self.press(Direction.RIGHT, 0.5)
                    self.press(Button.L, 0.05)
                print("判定中...")
                self.wait(2.6) #yaseino！からの時間調整
                if self.isContainTemplate('Encount_Ball4.png',0.8, show_value=False):
                    print("通常色")
                    while not (self.isContainTemplate('command.png', threshold=0.9, use_gray=True, show_value=False)):
                        self.wait(0.5)
                        print("wait...")
                    self.press(Direction.UP, 0.1)
                    self.wait(0.4)
                    self.press(Button.A,0.1,4.5)
                    print("試行回数",count,"回") #カウント
                    count += 1
                    if int(count) % 100 == 0: #ソフトリセットする倍数の設定。初期値は100です。
                        print("Reset Position")
                        self.press(Button.HOME, wait=2)
                        self.press(Button.X, wait=0.6)
                        self.press(Button.A, wait=2.5)  #closed
                        self.press(Button.A, wait=2.0)  #Choose Soft
                        self.press(Button.A, wait=2.0)  #User
                        self.press(Button.A, wait=14.0)  #loading Time（必要に応じて調整してください）
                        self.press(Button.A, wait=3.0)
                else:
                    print("色違い!!")
                    #self.press(Button.CAPTURE,3) #キャプチャー
                    self.finish()
