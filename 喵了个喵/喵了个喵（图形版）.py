#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
作  者    : 孙振光 light22@126.com
创建时间  : 2022-10-16 18:53:31
最后编辑  : 2022-10-16 19:30:38
编辑人    : 孙振光
'''
from 喵了个喵 import MiaoMiao
import PySimpleGUI as sg


class GuiMiao(MiaoMiao):
    def __init__(self) -> None:
        super().__init__()

    def play(self):
        layout = [
            [sg.Button(f"{self.l1[-1][0] if len(self.l1) != 0 else '    '}", key='-L1-'), sg.Button(
                f"{self.l2[-1][0] if len(self.l2) != 0 else '    '}", key='-L2-'), sg.Button(f"{self.l3[-1][0] if len(self.l3) != 0 else '    '}", key='-L3-')],
            [sg.Button(f"{self.l4[-1][0] if len(self.l4) != 0 else '    '}",key='-L4-'), sg.Button(
                f"{self.l5[-1][0] if len(self.l5) != 0 else '    '}",key='-L5-'), sg.Button(f"{self.l6[-1][0] if len(self.l6) != 0 else '    '}",key='-L6-')],
            [sg.Button(f"{self.l7[-1][0] if len(self.l7) != 0 else '    '}",key='-L7-'), sg.Button(
                f"{self.l8[-1][0] if len(self.l8) != 0 else '    '}",key='-L8-'), sg.Button(f"{self.l9[-1][0] if len(self.l9) != 0 else '    '}",key='-L9-')]
        ]

        window = sg.Window('喵了个喵', layout)

        while True:
            event, values = window.read()
            if event == None:
                break
            if event == '-L1-':
                self.select(self.l1)
            if event == '-L2-':
                self.select(self.l2)
            if event == '-L3-':
                self.select(self.l3)
            if event == '-L4-':
                self.select(self.l4)
            if event == '-L5-':
                self.select(self.l5)
            if event == '-L6-':
                self.select(self.l6)
            if event == '-L7-':
                self.select(self.l7)
            if event == '-L8-':
                self.select(self.l8)
            if event == '-L9-':
                self.select(self.l9)


if __name__ == '__main__':
    miao = GuiMiao()
    miao.play()
