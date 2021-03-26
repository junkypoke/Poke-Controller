#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Commands.PythonCommandBase import PythonCommand, ImageProcPythonCommand
from Commands.Keys import KeyPress, Button, Direction, Stick

class IMG_Check(ImageProcPythonCommand):
    NAME = 'IMG_Check'

    def __init__(self,cam):
        super().__init__(cam)

    def do(self):
        if self.isContainTemplate('Network_Offline.png',threshold=0.9, use_gray=False, show_value=True):
            #----.png -> 判定したいファイル名を入れる
            #threshold=0.9 ->0.9以上の時True
            #use_gray=True ->白黒画像で判定 / use_gray=False ->カラーで判定
            #show_value=True ->判定時の数値を表示する / show_value=True ->判定時の数値を表示しない
            print("True")
        print("Check_END")
