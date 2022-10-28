#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
作  者    : 孙振光 light22@126.com
创建时间  : 2022-10-16 18:53:31
最后编辑  : 2022-10-28 17:41:17
编辑人    : 孙振光
'''
from 喵了个喵 import MiaoMiao
import PySimpleGUI as sg


class GuiMiao(MiaoMiao):
    def __init__(self) -> None:
        super().__init__()
        

    def play(self):
        layout1 = [
            [sg.Button(f"{self.l1[-1][0] if self.l1 else '    '}",font=('黑体',24), key='-L1-',size=(9,4)), sg.Button(f"{self.l2[-1][0] if self.l2 else '    '}",font=('黑体',24), key='-L2-',size=(9,4)), sg.Button(f"{self.l3[-1][0] if self.l3 else '    '}",font=('黑体',24), key='-L3-',size=(9,4))],
            [sg.Button(f"{self.l4[-1][0] if self.l4 else '    '}",font=('黑体',24), key='-L4-',size=(9,4)), sg.Button(f"{self.l5[-1][0] if self.l5 else '    '}",font=('黑体',24), key='-L5-',size=(9,4)), sg.Button(f"{self.l6[-1][0] if self.l6 else '    '}",font=('黑体',24), key='-L6-',size=(9,4))],
            [sg.Button(f"{self.l7[-1][0] if self.l7 else '    '}",font=('黑体',24), key='-L7-',size=(9,4)), sg.Button(f"{self.l8[-1][0] if self.l8 else '    '}",font=('黑体',24), key='-L8-',size=(9,4)), sg.Button(f"{self.l9[-1][0] if self.l9 else '    '}",font=('黑体',24), key='-L9-',size=(9,4))]
        ]
        layout2 = [[sg.Button(i[0] if i else '',font=('黑体',16),key=f'-SPACE{x}-',size=(4,2)) for x,i in enumerate(self.space_l)]]
        layout = [
            [sg.Frame('请选择要放入空槽位的猫咪',layout1,size=(500,500))],
            [sg.Frame('空槽位',layout2,size=(500,90))],
            [sg.Text('')],
            [sg.T('by:',font=('黑体',12),text_color='red',size=40,justification='right'),sg.T('北极星光',font=('黑体',12),text_color='red')],
            [sg.T('E-mail:',font=('黑体',12),text_color='red',size=40,justification='right'),sg.T('light22@126.com',font=('黑体',12),text_color='red')]
        
        ]

        window = sg.Window('喵了个喵', layout, size=(500, 700),)
        while True:
            event, values = window.read()
            if event == None:
                break
            if event == '-L1-':
                self.select(self.l1)
                window['-L1-'].update(f"{self.l1[-1][0] if self.l1 else '    '}")
            if event == '-L2-':
                self.select(self.l2)
                window['-L2-'].update(f"{self.l2[-1][0] if self.l2 else '    '}")
            if event == '-L3-':
                self.select(self.l3)
                window['-L3-'].update(f"{self.l3[-1][0] if self.l3 else '    '}")
            if event == '-L4-':
                self.select(self.l4)
                window['-L4-'].update(f"{self.l4[-1][0] if self.l4 else '    '}")
            if event == '-L5-':
                self.select(self.l5)
                window['-L5-'].update(f"{self.l5[-1][0] if self.l5 else '    '}")
            if event == '-L6-':
                self.select(self.l6)
                window['-L6-'].update(f"{self.l6[-1][0] if self.l6 else '    '}")
            if event == '-L7-':
                self.select(self.l7)
                window['-L7-'].update(f"{self.l7[-1][0] if self.l7 else '    '}")
            if event == '-L8-':
                self.select(self.l8)
                window['-L8-'].update(f"{self.l8[-1][0] if self.l8 else '    '}")
            if event == '-L9-':
                self.select(self.l9)
                window['-L9-'].update(f"{self.l9[-1][0] if self.l9 else '    '}")
            for i in range(7):
                window[f'-SPACE{i}-'].update(self.space_l[i][0] if self.space_l[i] else '')
            if [] not in self.space_l:
                sg.popup('游戏结束！！！',font=('黑体',24),text_color='red')
                break
            if len(self.l1) + len(self.l2)+len(self.l3)+len(self.l4)+len(self.l5)+len(self.l6)+len(self.l7)+len(self.l8)+len(self.l9) == 0:
                sg.popup('恭喜通关！！！',font=('黑体',24),text_color='green')
                break

if __name__ == '__main__':
    miao = GuiMiao()
    miao.play()
