#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Commands.PythonCommandBase import PythonCommand, ImageProcPythonCommand
from Commands.Keys import KeyPress, Button, Direction, Stick

class Delibird_Search(ImageProcPythonCommand):
    NAME = 'JPN_★5デリバードレイド検索'

    def __init__(self,cam):
        super().__init__(cam)

    def do(self):
        print("-------------------------------")
        print("デリバード検索プログラム ver.1.0")
        print("Developed by.じゃんきー")
        print("-------------------------------")
        self.press(Button.B,0.1,0.6)
        count = 0

        while True:
            self.wait(0.5)
            print("wait...")
            if self.isContainTemplate('Network_Offline.png',0.7, show_value=False):
                print("Offline_Check")
                self.wait(1.0)
                self.press(Button.A, wait=1.0)
                self.press(Button.A)
                #ポケモンをかえるまで待機
                while not (self.isContainTemplate('raid_kaeru.png', threshold=0.85, use_gray=False, show_value=True)):
                    self.wait(0.5)
                    print("wait...")
                #日付変更
                self.press(Button.HOME, wait=2)
                self.press(Direction.DOWN)
                self.press(Direction.RIGHT)
                self.press(Direction.RIGHT)
                self.press(Direction.RIGHT)
                self.press(Direction.RIGHT)
                self.press(Direction.RIGHT)
                self.press(Button.A, wait=2.0)
                self.press(Direction.DOWN, duration=2.0, wait=0.2)
                self.press(Button.A, wait=0.5) #HONTAI
                self.press(Direction.DOWN)
                self.press(Direction.DOWN)
                self.press(Direction.DOWN)
                self.press(Direction.DOWN)
                self.press(Button.A, wait=0.5) #henkou
                self.press(Direction.DOWN)
                self.press(Direction.DOWN)
                self.press(Button.A) #日付変更
                self.press(Direction.LEFT, duration=0.7)
                self.press(Direction.RIGHT)
                self.press(Direction.RIGHT)
                self.press(Direction.UP)
                self.press(Direction.RIGHT, duration=0.7)
                self.press(Button.A, wait=1.0)
                self.press(Button.HOME, wait=1.0)
                self.press(Button.HOME, wait=2.0)
                #巣穴から出る
                self.press(Button.B, wait=1.0)
                self.press(Button.A, wait=2.0)
                while not (self.isContainTemplate('Network_Offline.png',0.7, show_value=True)):
                    self.wait(0.5)
                    print("wait...")
                self.press(Button.A, wait=1.0)
                if self.isContainTemplate('suana_energy.png',0.8, use_gray=True, show_value=True):
                    self.press(Button.A, wait=1.0)
                    self.press(Button.B, wait=3.0)
                print("Check...")
                #個体のチェック
                if self.isContainTemplate('star5.png',0.99, use_gray=False, show_value=True):
                    #star4.png(★4での検索) / star5.png(★5での検索)
                    self.wait(0.5)
                    print("Star_OK")
                    if self.isContainTemplate('Delibird_type.png',0.9, use_gray=False, show_value=True):
                        self.wait(0.5)
                        print("OK")
                        self.press(Button.B, wait=1.0)
                        print("FINISH")
                        self.finish()
                self.press(Button.B, wait=1.0)
                self.wait(0.5)
                print("継続")
                count += 1
                print("試行回数",count,"回") #カウント
