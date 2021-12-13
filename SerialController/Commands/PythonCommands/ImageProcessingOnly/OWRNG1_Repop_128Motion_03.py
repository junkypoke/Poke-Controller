#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Commands.PythonCommandBase import PythonCommand, ImageProcPythonCommand
from Commands.Keys import KeyPress, Button, Direction, Stick, Hat
import time
import os
from PIL import Image, ImageOps
import cv2
import numpy as np
from Commands.PythonCommands.ImageProcessingOnly import OWRNG0_Setting_03

class AutoEncount(ImageProcPythonCommand):
    NAME = 'OWRNG1_Repop128Motion_03'

    def __init__(self,cam):
        super().__init__(cam)

    def do(self):
        print("-------------------------------")
        print("OWRNG1_Repop_128Motion_03")
        print("Development:Junky/アキルノ/お修羅")
        print('')
        print('リポップで色違い捕獲後',OWRNG0_Setting_03.motion_full,'回 測定します')
        print("-------------------------------")
        self.wait(0.5)
        count = 0
        print("Start")

        #リポップからの色違い判定
        while True:
            self.wait(0.5)
            while not self.isContainTemplate('OWRNG/yasei.png', threshold=0.8, use_gray=True, show_value=False):
                self.press(Button.A, wait=0.3)
            print("判定中...")
            self.wait(OWRNG0_Setting_03.wait_yasei) #野生の！からの時間調整
            if self.isContainTemplate('OWRNG/Encount_Ball4.png',0.8, use_gray=False, show_value=False):
                self.wait(0.4)
                print("試行回数",count,"回")
                count += 1
                print("Reset")
                self.press(Button.HOME, wait=0.5)
                self.press(Button.X, wait=0.5)
                self.press(Button.A, wait=2.0)  #closed
            else:
                print("色違い!!")
                while not self.isContainTemplate('OWRNG/nigeru.png', threshold=0.8, use_gray=True, show_value=False):
                    self.press(Button.B,0.1,0.1)
				# ボール選択画面
                self.wait(1.5)
                self.press(Button.X,0.1,0.5)
                # マスターボールを認識するまで右キー入力
                while not self.isContainTemplate('OWRNG/MASTERBALL.png',threshold=0.7, use_gray=True, show_value=False):
                    self.press(Direction.RIGHT,0.1,0.5)
                    self.wait(0.1)
                print("\n［マスターボール］を使用します\n")
 				# マスターボールを選択して投げる
                self.press(Button.A,0.1,15.0)
                while not self.isContainTemplate('OWRNG/YY.png',threshold=0.8, use_gray=True, show_value=False):
                    self.press(Button.B,0.1,0.1)
                    self.wait(0.1)
                print("\nポケモンの捕獲が完了しました\n")
				# Xメニュー画面
                self.press(Button.X,0.05,0.1)
                while not self.isContainTemplate('OWRNG/POKEMON.png',threshold=0.8, use_gray=True, show_value=False):
                    self.wait(0.1)
				# ポケモンの画面を開く
                self.press(Button.A,0.05,0.1)
                while not self.isContainTemplate('OWRNG/X_POKEMON.png',threshold=0.8, use_gray=True, show_value=False):
                    self.wait(0.5)
                self.press(Button.A,0.05,1.0)
                self.press(Button.A,0.05,1.0)
                #self.press(Button.CAPTURE,3) #キャプチャー

                #ここからモーションのカウント
                self.wait(1.0)
                print('Motion Count Start!!')
                count2 = 0
                s = 'Motion:'
                print('')

                while count2 < OWRNG0_Setting_03.motion_full: #消費回数を入力する
                    self.press(Button.LCLICK,0.1,1.2)

                    #self.wait(0.1) # タイミング調整

                    # 閾値調整用
                    #self.isContainTemplate('butsuri.png',threshold=0.85, show_value=True)
                    # self.isContainTemplate('tokusyu.png',threshold=0.7, show_value=True)

                    if self.isContainTemplate('OWRNG/butsuri.png',threshold=0.8,show_value=False):
                        print(0 , end='')
                        s += str(0)
                    else:
                        print(1 , end='')
                        s += str(1)

                    self.wait(OWRNG0_Setting_03.wait_Lstick) # タイミング調整(LStickの入力が遅い場合は調整)
                    count2 += 1

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
